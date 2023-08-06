# pyRIST. Copyright 2019-2020 Mad Resistor LLP. All right reserved.
# Author: Kuldeep Singh Dhaka <kuldeep@madresistor.com>

from rist._binding import librist, ffi
from enum import Enum, IntEnum

class UrlParam(Enum):
	"""RIST URL Parameters name"""

	BUFFER_SIZE = "buffer"
	"""Buffer size argument"""

	SECRET = "secret"
	"""Secret argument"""

	AES_TYPE = "aes-type"
	"""AES Type argument"""

	BANDWIDTH = "bandwidth"
	"""Bandwidth argument"""

	RET_BANDWIDTH = "return-bandwidth"
	"""Return Bandwidth argument"""

	REORDER_BUFFER = "reorder-buffer"
	"""Reorder Buffer"""

	RTT = "rtt"
	"""Rount trip time argument"""

	COMPRESSION = "compression"
	"""Compression argument"""

	CNAME = "cname"
	"""Canonical Name argument"""

	VIRT_DST_PORT = "virt-dst-port"
	"""Virtual Destination Port argument"""

	WEIGHT = "weight"
	"""Weight argument"""

	MIFACE = "miface"
	"""Network Interface argument"""

	SESSION_TIMEOUT = "session-timeout"
	"""Session Timeout argument"""

	KEEPALIVE_INT = "keepalive-interval"
	"""Keepalive interval argument"""

	# Rist additional parameter names
	VIRT_SRC_PORT = "virt-src-port"
	"""Virtual Source Port argument"""

	PROFILE = "profile"
	"""Profile argument"""

	VERBOSE_LEVEL = "verbose-level"
	"""Verbose argument"""

class Nack(IntEnum):
	"""Negative Acknowledgement"""

	RANGE = librist.RIST_NACK_RANGE
	"""Range"""

	BITMASK = librist.RIST_NACK_BITMASK
	"""Bit Mask"""

class Profile(IntEnum):
	"""RIST protocol profile"""

	SIMPLE = librist.RIST_PROFILE_SIMPLE
	"""Simple profile"""

	MAIN = librist.RIST_PROFILE_MAIN
	"""Main profile"""

	ADVANCED = librist.RIST_PROFILE_ADVANCED
	"""Advanced profile"""

class LogLevel(IntEnum):
	"""Logging level"""

	QUIET = librist.RIST_LOG_QUIET
	"""Be Quiet (nothing)"""

	INFO = librist.RIST_LOG_INFO
	"""Informational only"""

	ERROR = librist.RIST_LOG_ERROR
	"""Error and lower only"""

	WARN = librist.RIST_LOG_WARN
	"""Warning and lower only"""

	DEBUG = librist.RIST_LOG_DEBUG
	"""Debug warning and lower"""

	SIMULATE = librist.RIST_LOG_SIMULATE
	"""Just like DEBUG but simulate error"""

class RecoveryMode(IntEnum):
	"""Recovery mode"""

	UNCONFIGURED = librist.RIST_RECOVERY_MODE_UNCONFIGURED
	"""Unconfigured"""

	DISABLED = librist.RIST_RECOVERY_MODE_DISABLED
	"""Disabled"""

	BYTES = librist.RIST_RECOVERY_MODE_BYTES
	"""Bytes"""

	TIME = librist.RIST_RECOVERY_MODE_TIME
	"""Time"""

class BufferBloatMode(IntEnum):
	"""Buffer Bloat Mode"""

	OFF = librist.RIST_BUFFER_BLOAT_MODE_OFF
	"""Off"""

	NORMAL = librist.RIST_BUFFER_BLOAT_MODE_NORMAL
	"""Normal"""

	AGGRESSIVE = librist.RIST_BUFFER_BLOAT_MODE_AGGRESSIVE
	"""Aggressive"""

class Peer(object):
	"""RIST Peer"""

	def __init__(self, ptr):
		self._ptr = ptr

	def __eq__(self, other):
		if not isinstance(other, Peer):
			# don't attempt to compare against unrelated types
			return NotImplemented

		return self._ptr == other._ptr

class OobBlock(object):
	"""Out Of Band"""

	def __init__(self, ptr):
		self._ptr = ptr

	@property
	def payload(self):
		"""Payload

		:returns: bytes
		"""

		return ffi.buffer(self._ptr.payload, self._ptr.payload_len)

	@property
	def peer(self):
		"""Peer

		:returns: rist.Peer
		"""

		return Peer(self._ptr.peer)

	@property
	def ts_ntp(self):
		"""Timestamp in NTP format.

		:returns: int
		"""

		return self._ptr.ts_ntp


class DataBlock(object):
	"""RIST Data"""

	def __init__(self, ptr):
		self._ptr = ptr

	@property
	def flow_id(self):
		"""Flow ID

		:returns: int
		"""

		return self._ptr.flow_id

	@property
	def seq(self):
		"""Sequence number

		:returns: int
		"""

		return self._ptr.seq

	@property
	def flags(self):
		"""Flags

		:returns: int
		"""

		return self._ptr.flags

	@property
	def virt_src_port(self):
		"""Virtual source port

		:returns: int
		"""

		return self._ptr.virt_src_port

	@property
	def virt_dst_port(self):
		"""Virtual destination port

		:returns: int
		"""

		return self._ptr.virt_dst_port

	@property
	def payload(self):
		"""Payload

		:returns: bytes
		"""

		return ffi.buffer(self._ptr.payload, self._ptr.payload_len)

	@property
	def peer(self):
		"""Peer

		:returns: rist.Peer
		"""

		return Peer(self._ptr.peer)

	@property
	def ts_ntp(self):
		"""Timestamp in NTP format.

		:returns: int
		"""

		return self._ptr.ts_ntp
