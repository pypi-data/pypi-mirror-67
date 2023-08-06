# pyRIST. Copyright 2019-2020 Mad Resistor LLP. All right reserved.
# Author: Kuldeep Singh Dhaka <kuldeep@madresistor.com>

from rist._binding import ffi, librist
from rist.exceptions import ResultException
from rist.misc import Peer, DataBlock, Profile, LogLevel
from rist.common import common_destroy,\
	common_auth_handler_set, common_start, common_jitter_max_set, \
	common_nack_type_set, common_peer_create, common_peer_destroy, \
	common_oob_callback_set, common_oob_write, common_oob_read

class Receiver(object):
	"""RIST Receiver"""

	_create = librist.rist_receiver_create
	_auth_handler_set = librist.rist_receiver_auth_handler_set
	_peer_create = librist.rist_receiver_peer_create
	_peer_destroy = librist.rist_receiver_peer_destroy
	_jitter_max_set = librist.rist_receiver_jitter_max_set
	_oob_callback_set = librist.rist_receiver_oob_callback_set
	_nack_type_set = librist.rist_receiver_nack_type_set
	_start = librist.rist_receiver_start
	_oob_write = librist.rist_receiver_oob_write
	_oob_read = librist.rist_receiver_oob_read
	_data_read = librist.rist_receiver_data_read
	_destroy = librist.rist_receiver_destroy

	def __init__(self, profile=Profile.MAIN, log_level=LogLevel.WARN):
		"""Create an instance of Receiver

		:param profile: RIST profile (:class:`rist.PROFILE_SIMPLE`, :class:`rist.PROFILE_MAIN` [default], :class:`rist.PROFILE_ADVANCED`)
		:param log_level: Log level (:class:`rist.LOG_QUIET`, :class:`rist.LOG_INFO`, :class:`rist.LOG_ERROR`, :class:`rist.LOG_WARN` [default], :class:`rist.LOG_DEBUG`, :class:`rist.LOG_SIMULATE`)
		:raises: :class:`rist.ResultException`
		"""

		ptr_ptr = ffi.new("struct rist_receiver **")
		res = self._create(ptr_ptr, profile.value, log_level.value)
		ResultException.act(res)
		self._ptr = ptr_ptr[0]

	__del__ = common_destroy
	auth_handler_set = common_auth_handler_set
	start = common_start
	jitter_max_set = common_jitter_max_set
	nack_type_set = common_nack_type_set
	peer_create = common_peer_create
	peer_destroy = common_peer_destroy
	oob_callback_set = common_oob_callback_set
	oob_write = common_oob_write
	oob_read = common_oob_read

	def data_read(self, timeout=0):
		"""Read received data.

		:param int timeout: Timeout in milliseconds to wait for Queue.
		:returns: rist.DataBlock
		:raises: :class:`rist.ResultException`
		"""

		ptr_ptr = ffi.new("struct rist_data_block **")
		ResultException.act(self._data_read(self._ptr, ptr_ptr, timeout))
		ptr = ptr_ptr[0]
		return None if ptr == ffi.NULL else DataBlock(ptr)
