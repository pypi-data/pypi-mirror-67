import math
import time
import threading
import RNS
import RNS.vendor.umsgpack as msgpack

APP_NAME = "lxmf"

class LXMessage:
	DRAFT           = 0x00
	OUTBOUND        = 0x01
	SENDING         = 0x02
	SENT            = 0x04
	DELIVERED       = 0x08
	states          = [DRAFT, OUTBOUND, SENDING, SENT, DELIVERED]

	UNKNOWN         = 0x00
	PACKET          = 0x01
	RESOURCE        = 0x02
	representations = [UNKNOWN, PACKET, RESOURCE]

	OPPORTUNISTIC   = 0x01
	DIRECT          = 0x02
	PROPAGATED      = 0x03
	valid_methods   = [OPPORTUNISTIC, DIRECT, PROPAGATED]

	DESTINATION_LENGTH = RNS.Identity.TRUNCATED_HASHLENGTH//8
	SIGNATURE_LENGTH   = RNS.Identity.SIGLENGTH//8

	# LXMF overhead is 163 bytes per message:
	#   10  bytes for destination hash
	#   10  bytes for source hash
	#   128 bytes for RSA signature
	#   8   bytes for timestamp
	#   7   bytes for msgpack structure
	LXMF_OVERHEAD  = 2*DESTINATION_LENGTH + SIGNATURE_LENGTH + 8 + 7

	# With an MTU of 500, the maximum RSA-encrypted
	# amount of data we can send in a single packet
	# is given by the below calculation; 258 bytes.
	RSA_PACKET_MDU = RNS.Packet.RSA_MDU
	
	# The max content length we can fit in LXMF message
	# inside a single RNS packet is the RSA MDU, minus
	# the LXMF overhead. We can optimise a bit though, by
	# inferring the destination hash from the destination
	# field of the packet, therefore we also add the length
	# of a destination hash to the calculation. With default
	# RNS and LXMF parameters, the largest single-packet
	# LXMF message we can send is 105 bytes. If a message
	# is larger than that, a Reticulum link will be used.
	RSA_PACKET_MAX_CONTENT = RSA_PACKET_MDU - LXMF_OVERHEAD + DESTINATION_LENGTH
	
	# Links can carry a significantly larger MDU, due to
	# more efficient elliptic curve cryptography. The link
	# MDU with default Reticulum parameters is 415 bytes.
	LINK_PACKET_MDU = RNS.Link.MDU

	# Which means that we can deliver single-packet LXMF
	# messages with content of up to 252 bytes over a link.
	# If a message is larger than that, LXMF will sequence
	# and transfer it as a RNS resource over the link instead.
	LINK_PACKET_MAX_CONTENT = LINK_PACKET_MDU - LXMF_OVERHEAD

	# For plain packets without encryption, we can
	# fit up to 324 bytes of content.
	PLAIN_PACKET_MDU = RNS.Packet.PLAIN_MDU
	PLAIN_PACKET_MAX_CONTENT = PLAIN_PACKET_MDU - LXMF_OVERHEAD + DESTINATION_LENGTH

	def __init__(self, destination, source, content = "", title = "", fields = None, desired_method = None, destination_hash = None, source_hash = None):
		if isinstance(destination, RNS.Destination) or destination == None:
			self.__destination    = destination
			if destination != None:
				self.destination_hash = destination.hash
			else:
				self.destination_hash = destination_hash
		else:
			raise ValueError("LXMessage initialised with invalid destination")

		if isinstance(source, RNS.Destination) or source == None:
			self.__source    = source
			if source != None:
				self.source_hash = source.hash
			else:
				self.source_hash = source_hash
		else:
			raise ValueError("LXMessage initialised with invalid source")

		self.set_title_from_string(title)
		self.set_content_from_string(content)

		self.set_fields(fields)

		self.payload      = None
		self.timestamp    = None
		self.signature    = None
		self.hash         = None
		self.packed       = None
		self.progress     = None
		self.state        = LXMessage.DRAFT
		self.method       = LXMessage.UNKNOWN

		self.representation          = LXMessage.UNKNOWN
		self.desired_method          = desired_method
		self.delivery_attempts       = 0
		self.transport_encryption    = None
		self.packet_representation   = None
		self.resource_representation = None
		self.__delivery_destination  = None

	def set_title_from_string(self, title_string):
		self.title = title_string.encode("utf-8")

	def set_title_from_bytes(self, title_bytes):
		self.title = title_bytes

	def title_as_string(self):
		return self.title.decode("utf-8")

	def set_content_from_string(self, content_string):
		self.content = content_string.encode("utf-8")

	def set_content_from_bytes(self, content_bytes):
		self.content = content_bytes

	def content_as_string(self):
		return self.content.decode("utf-8")

	def set_fields(self, fields):
		if isinstance(fields, dict) or fields == None:
			self.fields = fields
		else:
			raise ValueError("LXMessage property \"fields\" can only be dict or None")

	def get_fields(self):
		return self.__fields

	def set_destination(self, destination):
		if self.destination == None:
			if isinstance(destination, RNS.Destination):
				self.__destination = destination
			else:
				raise ValueError("Invalid destination set on LXMessage")
		else:
			raise ValueError("Cannot reassign destination on LXMessage")

	def get_destination(self):
		return self.__destination

	def set_source(self, source):
		if self.source == None:
			if isinstance(source, RNS.Destination):
				self.__source = source
			else:
				raise ValueError("Invalid source set on LXMessage")
		else:
			raise ValueError("Cannot reassign source on LXMessage")

	def get_source(self):
		return self.__source

	def set_delivery_destination(self, delivery_destination):
		self.__delivery_destination = delivery_destination

	def pack(self):
		self.timestamp = time.time()
		self.payload = [self.timestamp, self.title, self.content, self.fields]

		hashed_part      = b""
		hashed_part     += self.__destination.hash
		hashed_part     += self.__source.hash
		hashed_part     += msgpack.packb(self.payload)
		self.hash        = RNS.Identity.fullHash(hashed_part)
		self.message_id  = self.hash
		
		signed_part      = b""
		signed_part     += hashed_part
		signed_part     += self.hash
		self.signature   = self.__source.sign(signed_part)

		self.packed      = b""
		self.packed     += self.__destination.hash
		self.packed     += self.__source.hash
		self.packed     += self.signature
		packed_payload   = msgpack.packb(self.payload)
		self.packed     += packed_payload
		self.packed_size = len(self.packed)
		content_size     = len(packed_payload)

		# If no desired delivery method has been defined,
		# one will be chosen according to these rules:
		if self.desired_method == None:
			self.desired_method == LXMessage.DIRECT
		# TODO: Expand rules to something more intelligent

		if self.desired_method == LXMessage.OPPORTUNISTIC:
			if self.__destination.type == RNS.Destination.SINGLE:
				single_packet_content_limit = LXMessage.RSA_PACKET_MAX_CONTENT
			elif self.__destination.type == RNS.Destination.PLAIN:
				single_packet_content_limit = LXMessage.PLAIN_PACKET_MAX_CONTENT

			if content_size > single_packet_content_limit:
				raise TypeError("LXMessage desired opportunistic delivery method, but content exceeds single-packet size.")
			else:
				self.method = LXMessage.OPPORTUNISTIC
				self.representation = LXMessage.PACKET
				self.__delivery_destination = self.__destination

		elif self.desired_method == LXMessage.DIRECT or self.desired_method == LXMessage.PROPAGATED:
			single_packet_content_limit = LXMessage.LINK_PACKET_MAX_CONTENT
			if content_size <= single_packet_content_limit:
				self.method = self.desired_method
				self.representation = LXMessage.PACKET
			else:
				self.method = self.desired_method
				self.representation = LXMessage.RESOURCE

	def send(self):
		if self.method == LXMessage.OPPORTUNISTIC:
			self.__as_packet().send().delivery_callback(self.__mark_delivered)
			self.state = LXMessage.SENT
		elif self.method == LXMessage.DIRECT:
			self.state = LXMessage.SENDING
			self.resource_representation = self.__as_resource()
		elif self.method == LXMessage.PROPAGATED:
			pass

	def __mark_delivered(self, receipt = None):
		RNS.log("Received delivery notification for "+str(self), RNS.LOG_DEBUG)
		self.state = LXMessage.DELIVERED

	def __resource_concluded(self, resource):
		if resource.status == RNS.Resource.COMPLETE:
			self.__mark_delivered()
		else:
			resource.link.teardown()
			self.state = LXMessage.OUTBOUND


	def __update_transfer_progress(self, resource):
		self.progress = resource.progress()

	def __as_packet(self):
		if not self.packed:
			self.pack()

		if not self.__delivery_destination:
			raise ValueError("Can't synthesize packet for LXMF message before delivery destination is known")

		if self.method == LXMessage.OPPORTUNISTIC:
			return RNS.Packet(self.__delivery_destination, self.packed[LXMessage.DESTINATION_LENGTH:])
		elif self.method == LXMessage.DIRECT or self.method == LXMessage.PROPAGATED:
			return RNS.Packet(self.__delivery_destination, self.packed)

	def __as_resource(self):
		if not self.packed:
			self.pack()

		if not self.__delivery_destination:
			raise ValueError("Can't synthesize resource for LXMF message before delivery destination is known")

		if not self.__delivery_destination.type == RNS.Destination.LINK:
			raise TypeError("Tried to synthesize resource for LXMF message on a delivery destination that was not a link")

		if not self.__delivery_destination.status == RNS.Link.ACTIVE:
			raise ConnectionError("Tried to synthesize resource for LXMF message on a link that was not active")

		self.progress = 0.0
		return RNS.Resource(self.packed, self.__delivery_destination, callback = self.__resource_concluded, progress_callback = self.__update_transfer_progress)

	@staticmethod
	def unpack_from_bytes(lxmf_bytes):
		destination_hash = lxmf_bytes[:LXMessage.DESTINATION_LENGTH]
		source_hash      = lxmf_bytes[LXMessage.DESTINATION_LENGTH:2*LXMessage.DESTINATION_LENGTH]
		signature        = lxmf_bytes[2*LXMessage.DESTINATION_LENGTH:2*LXMessage.DESTINATION_LENGTH+LXMessage.SIGNATURE_LENGTH]
		packed_payload   = lxmf_bytes[2*LXMessage.DESTINATION_LENGTH+LXMessage.SIGNATURE_LENGTH:]
		unpacked_payload = msgpack.unpackb(packed_payload)
		destination      = RNS.Identity.recall(destination_hash)
		source           = RNS.Identity.recall(source_hash)
		timestamp        = unpacked_payload[0]
		title_bytes      = unpacked_payload[1]
		content_bytes    = unpacked_payload[2]
		fields           = unpacked_payload[3]

		message = LXMessage(
			destination = destination,
			source = source,
			content = "",
			title = "",
			fields = fields,
			destination_hash = destination_hash,
			source_hash = source_hash)

		message.set_title_from_bytes(title_bytes)
		message.set_content_from_bytes(content_bytes)
		message.timestamp = timestamp

		return message

	@staticmethod
	def unpack_from_file(lxmf_file_handle):
		pass

class LXMRouter:
	MAX_DELIVERY_ATTEMPTS = 3
	PROCESSING_INTERVAL   = 5
	DELIVERY_RETRY_WAIT   = 15

	def __init__(self):
		self.pending_inbound       = []
		self.pending_outbound      = []
		self.failed_outbound       = []
		self.direct_links          = {}
		self.delivery_destinations = {}

		self.processing_outbound = False
		self.processing_inbound  = False

		self.identity = RNS.Identity()
		self.lxmf_query_destination  = RNS.Destination(None, RNS.Destination.IN, RNS.Destination.PLAIN, APP_NAME, "query")
		self.propagation_destination = RNS.Destination(self.identity, RNS.Destination.IN, RNS.Destination.SINGLE, APP_NAME, "propagation")

		self.__delivery_callback = None

		job_thread = threading.Thread(target=self.jobloop)
		job_thread.setDaemon(True)
		job_thread.start()

	def register_delivery_identity(self, identity, display_name = None):
		delivery_destination = RNS.Destination(identity, RNS.Destination.IN, RNS.Destination.SINGLE, "lxmf", "delivery")
		delivery_destination.packet_callback(self.delivery_packet)
		delivery_destination.link_established_callback(self.delivery_link_established)
		delivery_destination.display_name = display_name

		self.delivery_destinations[delivery_destination.hash] = delivery_destination
		return delivery_destination

	def register_delivery_callback(self, callback):
		self.__delivery_callback = callback

	def handle_outbound(self, lxmessage):
		RNS.log("LXM Router received outbound message: "+str(lxmessage))
		while self.processing_outbound:
			time.sleep(0.1)

		if not lxmessage.packed:
			lxmessage.pack()

		self.pending_outbound.append(lxmessage)
		self.process_outbound()

	def lxmf_delivery(self, lxmf_data, destination_type = None):
		try:
			message = LXMessage.unpack_from_bytes(lxmf_data)
		except Exception as e:
			RNS.log("Could not assemble LXMF message from received data", RNS.LOG_NOTICE)
			RNS.log("The contained exception was: "+str(e), RNS.LOG_DEBUG)

		if RNS.Reticulum.should_allow_unencrypted():
			message.transport_encryption = "Consider unencrypted (Disabling encryption was allowed in Reticulum configuration)"
		else:
			if destination_type == RNS.Destination.SINGLE:
				message.transport_encryption = "RSA-"+str(RNS.Identity.KEYSIZE)
			elif destination_type == RNS.Destination.GROUP:
				message.transport_encryption = "AES-128"
			elif destination_type == RNS.Destination.LINK:
				message.transport_encryption = "EC-SECP256R1"
			else:
				message.transport_encryption = None

		if self.__delivery_callback != None:
			self.__delivery_callback(message)

		return True

	def delivery_packet(self, data, packet):
		try:
			if packet.destination.type != RNS.Destination.LINK:
				lxmf_data  = b""
				lxmf_data += packet.destination.hash
				lxmf_data += data
			else:
				lxmf_data = data

			if self.lxmf_delivery(lxmf_data, packet.destination.type):
				packet.prove()

		except Exception as e:
			RNS.log("Exception occurred while parsing incoming LXMF data.", RNS.LOG_ERROR)
			RNS.log("The contained exception was: "+str(e), RNS.LOG_ERROR)

	def delivery_link_established(self, link):
		link.packet_callback(self.delivery_packet)
		link.set_resource_strategy(RNS.Link.ACCEPT_ALL)
		link.resource_started_callback(self.resource_transfer_began)
		link.resource_concluded_callback(self.resource_transfer_concluded)

	def delivery_link_closed(self, link):
		pass

	def resource_transfer_began(self, resource):
		RNS.log("Transfer began for resource "+str(resource), RNS.LOG_DEBUG)

	def resource_transfer_concluded(self, resource):
		RNS.log("Transfer concluded for resource "+str(resource), RNS.LOG_DEBUG)
		if resource.status == RNS.Resource.COMPLETE:
			self.lxmf_delivery(resource.data, resource.link.type)

	def jobloop(self):
		while (True):
			# TODO: Improve this to scheduling, so manual
			# triggers can delay next run
			self.jobs()
			time.sleep(LXMRouter.PROCESSING_INTERVAL)

	def jobs(self):
		self.process_outbound()

	def process_outbound(self, sender = None):
		if self.processing_outbound:
			return

		for lxmessage in self.pending_outbound:
			if lxmessage.state == LXMessage.DELIVERED:
				RNS.log("Delivery has occurred for "+str(lxmessage)+", removing from outbound queue", RNS.LOG_DEBUG)
				self.pending_outbound.remove(lxmessage)
			else:	
				RNS.log("Starting outbound processing for "+str(lxmessage)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
				# Outbound handling for opportunistic messages
				if lxmessage.method == LXMessage.OPPORTUNISTIC:				
					if lxmessage.delivery_attempts < LXMRouter.MAX_DELIVERY_ATTEMPTS:
						if not hasattr(lxmessage, "next_delivery_attempt") or time.time() > lxmessage.next_delivery_attempt:
							lxmessage.delivery_attempts += 1
							lxmessage.next_delivery_attempt = time.time() + LXMRouter.DELIVERY_RETRY_WAIT
							RNS.log("Opportunistic delivery attempt "+str(lxmessage.delivery_attempts)+" for "+str(lxmessage)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
							lxmessage.send()
					else:
						RNS.log("Max delivery attempts reached for "+str(lxmessage)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
						self.pending_outbound.remove(lxmessage)
						self.failed_outbound.append(lxmessage)

				# Outbound handling for messages transferred
				# over a direct link to the final recipient
				elif lxmessage.method == LXMessage.DIRECT:
					if lxmessage.delivery_attempts < LXMRouter.MAX_DELIVERY_ATTEMPTS:
						delivery_destination_hash = lxmessage.get_destination().hash

						if delivery_destination_hash in self.direct_links:
							# A link already exists, so we'll try to use it
							# to deliver the message
							direct_link = self.direct_links[delivery_destination_hash]
							if direct_link.status == RNS.Link.ACTIVE:
								if lxmessage.state != LXMessage.SENDING:
									RNS.log("Starting transfer of "+str(lxmessage)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
									lxmessage.set_delivery_destination(direct_link)
									lxmessage.send()
								else:
									RNS.log("The transfer of "+str(lxmessage)+" is in progress ("+str(round(lxmessage.progress*100, 1))+"%)", RNS.LOG_DEBUG)
							elif direct_link.status == RNS.Link.CLOSED:
								RNS.log("The link to "+RNS.prettyhexrep(lxmessage.get_destination().hash)+" was closed", RNS.LOG_DEBUG)
								lxmessage.set_delivery_destination(None)
								self.direct_links.pop(delivery_destination_hash)
								lxmessage.next_delivery_attempt = time.time() + LXMRouter.DELIVERY_RETRY_WAIT
							else:
								# Simply wait for the link to become
								# active or close
								RNS.log("The link to "+RNS.prettyhexrep(lxmessage.get_destination().hash)+" is pending, waiting for link to become active", RNS.LOG_DEBUG)
						else:
							# No link exists, so we'll try to establish one, but
							# only if we've never tried before, or the retry wait
							# period has elapsed.
							if not hasattr(lxmessage, "next_delivery_attempt") or time.time() > lxmessage.next_delivery_attempt:
								lxmessage.delivery_attempts += 1
								lxmessage.next_delivery_attempt = time.time() + LXMRouter.DELIVERY_RETRY_WAIT
								if lxmessage.delivery_attempts < LXMRouter.MAX_DELIVERY_ATTEMPTS:
									RNS.log("Establishing link to "+RNS.prettyhexrep(lxmessage.get_destination().hash)+" for delivery attempt "+str(lxmessage.delivery_attempts)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
									delivery_link = RNS.Link(lxmessage.get_destination())
									delivery_link.link_established_callback(self.process_outbound)
									self.direct_links[delivery_destination_hash] = delivery_link
					else:
						RNS.log("Max delivery attempts reached for "+str(lxmessage)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
						self.pending_outbound.remove(lxmessage)
						self.failed_outbound.append(lxmessage)

				# Outbound handling for messages transported via
				# propagation to a LXMF router network.
				elif lxmessage.method == LXMessage.PROPAGATED:
					RNS.log("Attempting propagated delivery for "+str(lxmessage)+" to "+RNS.prettyhexrep(lxmessage.get_destination().hash), RNS.LOG_DEBUG)
					raise NotImplementedError("LXMF propagation is not implemented yet")