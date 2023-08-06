# pyRIST. Copyright 2019-2020 Mad Resistor LLP. All right reserved.
# Author: Kuldeep Singh Dhaka <kuldeep@madresistor.com>

from rist._binding import ffi, librist
from rist.exceptions import ResultException
from rist.misc import Peer, DataBlock, Profile, LogLevel
from rist.common import common_destroy, common_start, \
	common_auth_handler_set, common_flow_id_get, \
	common_jitter_max_set, common_peer_create, common_peer_destroy, \
	common_oob_callback_set, common_oob_write, common_oob_read

@ffi.callback("void(void *, const struct rist_data_block *)")
def glue_data_callback(arg, data_block):
	"""Handle Data callback from librist."""

	h = ffi.from_handle(arg)
	h._data_callback(DataBlock(data_block))

class Sender(object):
	"""RIST Sender"""

	_create = librist.rist_sender_create
	_destroy = librist.rist_sender_destroy
	_start = librist.rist_sender_start
	_auth_handler_set = librist.rist_sender_auth_handler_set
	_peer_create = librist.rist_sender_peer_create
	_peer_destroy = librist.rist_sender_peer_destroy
	_jitter_max_set = librist.rist_sender_jitter_max_set
	_oob_callback_set = librist.rist_sender_oob_callback_set
	_oob_write = librist.rist_sender_oob_write
	_oob_read = librist.rist_sender_oob_read
	_data_write = librist.rist_sender_data_write
	_flow_id_get = librist.rist_sender_flow_id_get
	_data_callback_set = librist.rist_receiver_data_callback_set

	def __init__(self, profile=Profile.MAIN, flow_id=0, log_level=LogLevel.WARN):
		"""Create an instance of Receiver

		:param profile: RIST profile (:class:`rist.PROFILE_SIMPLE`, :class:`rist.PROFILE_MAIN` [default], :class:`rist.PROFILE_ADVANCED`)
		:param int flow_id: Flow ID (0 to autogenerate)
		:param log_level: Log level (:class:`rist.LOG_QUIET`, :class:`rist.LOG_INFO`, :class:`rist.LOG_ERROR`, :class:`rist.LOG_WARN` [default], :class:`rist.LOG_DEBUG`, :class:`rist.LOG_SIMULATE`)
		:raises: :class:`rist.ResultException`
		"""

		ptr_ptr = ffi.new("struct rist_sender **")
		res = self._create(ptr_ptr, profile.value, flow_id, log_level.value)
		ResultException.act(res)
		self._ptr = ptr_ptr[0]

	__del__ = common_destroy
	start = common_start
	auth_handler_set = common_auth_handler_set
	flow_id_get = common_flow_id_get
	jitter_max_set = common_jitter_max_set
	peer_create = common_peer_create
	peer_destroy = common_peer_destroy
	oob_callback_set = common_oob_callback_set
	oob_write = common_oob_write
	oob_read = common_oob_read

	def data_callback_set(self, cb=None):
		"""Get data via callback

		:param callable cb: Callback
		:raises: :class:`rist.ResultException`
		"""

		h = ffi.NULL if cb is None else ffi.new_handle(self)
		_cb = ffi.NULL if cb is None else glue_data_callback
		ResultException.act(self._data_callback_set(self._ptr, _cb, h))
		self._data_callback = cb

	def data_write(self, payload, virt_src_port=librist.RIST_DEFAULT_VIRT_SRC_PORT, ts_ntp=0):
		"""Send data to :class:`rist.Receiver`.

		:param bytes payload: Payload.
		:param int virt_src_port: Virtual source port (unused in simple profile).
		:param int ts_ntp: Timestamp in NTP format (if 0, autogenerate internally).
		:returns: int. -- number of written bytes
		:raises: :class:`rist.ResultException`
		"""

		payload = ffi.from_buffer(payload)
		block = ffi.new("struct rist_data_block *", {
			'payload': payload,
			'payload_len': len(payload),
			'virt_src_port': virt_src_port,
			'ts_ntp': ts_ntp
		})

		return ResultException.act(self._data_write(self._ptr, block))
