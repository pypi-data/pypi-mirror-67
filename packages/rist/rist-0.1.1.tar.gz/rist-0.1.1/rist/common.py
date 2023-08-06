# pyRIST. Copyright 2019-2020 Mad Resistor LLP. All right reserved.
# Author: Kuldeep Singh Dhaka <kuldeep@madresistor.com>

from rist._binding import ffi, librist
from rist.exceptions import ResultException, RejectPeerException
from rist.misc import Peer, DataBlock, OobBlock, RecoveryMode, BufferBloatMode

@ffi.callback("void(void *, struct rist_peer *)")
def glue_auth_handler_disconn(arg, peer):
	"""Handle Auth disconnect callback from librist"""

	h = ffi.from_handle(arg)
	h._auth_handler_disconn_callback(Peer(peer))

@ffi.callback("int(void *, const char *, uint16_t, const char *, uint16_t, struct rist_peer *)")
def glue_auth_handler_conn(arg, conn_ip, conn_port, local_ip, local_port, peer):
	"""Handle Auth connect callback from librist"""

	h = ffi.from_handle(arg)
	_conn_ip = None if (conn_ip == ffi.NULL) else ffi.string(conn_ip)
	_local_ip = None if (local_ip == ffi.NULL) else ffi.string(local_ip)
	try:
		h._auth_handler_conn_callback(_conn_ip, conn_port, _local_ip, local_port, Peer(peer))
		return 0

	# Exception raised by callback
	except RejectPeerException as e: return -1

@ffi.callback("void(void *, const struct rist_oob_block *)")
def glue_oob_callback(arg, oob_block):
	"""Handle OOB callback from librist."""

	h = ffi.from_handle(arg)
	h._oob_callback(OobBlock(oob_block))

# set @a h to None to remove the handler
def common_auth_handler_set(self, conn, disconn):
	"""Set peer authentication handler.

	:param conn: Connect callback (pass *None* to disable)
	:param disconn: Disconnect callback (pass *None* to disable)
	:raises: :class:`rist.ResultException`

	.. note::
		If *conn* callback raises :class:`rist.RejectPeerException`, peer is rejected.
	"""

	h = ffi.NULL if conn is None and disconn is None else ffi.new_handle(self)
	_conn = ffi.NULL if conn is None else glue_auth_handler_conn
	_disconn = ffi.NULL if disconn is None else glue_auth_handler_disconn
	ResultException.act(self._auth_handler_set(self._ptr, _conn, _disconn, h))
	self._auth_handler_conn_callback = conn
	self._auth_handler_disconn_callback = disconn

def common_start(self):
	"""Start communicating.

	:raises: :class:`rist.ResultException`
	"""

	ResultException.act(self._start(self._ptr))

def common_destroy(self):
	"""Destroy the object.

	:raises: :class:`rist.ResultException`
	"""

	ResultException.act(self._destroy(self._ptr))
	del self._ptr

def common_nack_type_set(self, val):
	"""Set NACK type.

	:param str val: :class:`rist.NACK_RANGE` or :class:`NACK_BITMASK`
	:raises: :class:`rist.ResultException`
	"""

	ResultException.act(self._nack_type_set(self._ptr, val.value))

def common_jitter_max_set(self, ms):
	"""Set maximum jitter value.

	:param int ms: milliseconds
	:raises: :class:`rist.ResultException`
	"""

	ResultException.act(self._jitter_max_set(self._ptr, ms))

# FIXME: since we have a versioning system.
#  only make sure those properties are accepted that are part of the struct
def build_peer_config(config):
	default = {
		'virt_dst_port': librist.RIST_DEFAULT_VIRT_DST_PORT,

		'recovery_mode': RecoveryMode.TIME,
		'recovery_maxbitrate': librist.RIST_DEFAULT_RECOVERY_MAXBITRATE,
		'recovery_maxbitrate_return': librist.RIST_DEFAULT_RECOVERY_MAXBITRATE_RETURN,
		'recovery_length_min': librist.RIST_DEFAULT_RECOVERY_LENGHT_MIN,
		'recovery_length_max': librist.RIST_DEFAULT_RECOVERY_LENGHT_MAX,
		'recovery_reorder_buffer': librist.RIST_DEFAULT_RECOVERY_REORDER_BUFFER,
		'recovery_rtt_min': librist.RIST_DEFAULT_RECOVERY_RTT_MIN,
		'recovery_rtt_max': librist.RIST_DEFAULT_RECOVERY_RTT_MAX,

		'weight': 0,
		'compression': 1,
		'key_size': 0,
		'key_rotation': 0,

		'buffer_bloat_mode': BufferBloatMode.OFF,
		'buffer_bloat_limit': librist.RIST_DEFAULT_BUFFER_BLOAT_LIMIT,
		'buffer_bloat_hard_limit': librist.RIST_DEFAULT_BUFFER_BLOAT_HARD_LIMIT,

		'session_timeout': librist.RIST_DEFAULT_SESSION_TIMEOUT,
		'keepalive_interval': librist.RIST_DEFAULT_KEEPALIVE_INTERVAL
	}


	config = dict(config)
	config.update(default)

	# string
	for i in ('address', ):
		if not isinstance(config[i], bytes):
			config[i] = bytes(config[i], "utf-8")

	# boolean
	for i in ('initiate_conn', ):
		# if not present, will automaticall means false
		if i not in config: continue

		if not isinstance(config[i], int):
			config[i] = int(config[i])

	override = {
		'version': librist.RIST_PEER_CONFIG_VERSION
	}

	config.update(override)

	return config

def common_peer_create(self, config):
	"""Create a new peer.

	:param dict config: Peer configuration
	:returns: rist.Peer
	:raises: :class:`rist.ResultException`

	.. note::
		*config* argument can contain the following fields:

		*initiate_conn*: 1 => Initiate connection, 0 => bind to interface.

		*address*: Address of peer or network interface IP to bind to.

		*physical_port*: Port of peer or port to bind to.

		*virt_dst_port*: See librist docs (not required in SIMPLE profile)

		*recovery_mode*: :class:`rist.RECOVERY_MODE_UNCONFIGURED`, :class:`rist.RECOVERY_MODE_DISABLED`, :class:`rist.RECOVERY_MODE_BYTES`, :class:`rist.RECOVERY_MODE_TIME`

		*recovery_maxbitrate*: See librist docs

		*recovery_maxbitrate_return*: See librist docs

		*recovery_length_min*: See librist docs

		*recovery_length_max*: See librist docs

		*recovery_reorder_buffer*: See librist docs

		*recovery_rtt_min*: See librist docs

		*recovery_rtt_max*: See librist docs

		*weight*: See librist docs

		*buffer_bloat_mode*: :class:`rist.BUFFER_BLOAT_MODE_OFF`, :class:`librist.RIST_BUFFER_BLOAT_MODE_NORMAL`, :class:`librist.RIST_BUFFER_BLOAT_MODE_AGGRESSIVE`

		*buffer_bloat_limit*: See librist docs

		*buffer_bloat_hard_limit*: See librist docs
	"""

	if isinstance(config, str):
		# address not a dict
		config_p = ffi.new("struct rist_peer *")
		config_pp = ffi.new("struct rist_peer **", config_p)
		ResultException.act(librist.rist_parse_address(config, config_pp))
	else:
		config = build_peer_config(config)
		config_p = ffi.new("struct rist_peer_config *", config)

	peer_pp = ffi.new("struct rist_peer **")
	ResultException.act(self._peer_create(self._ptr, peer_pp, config_p))
	return Peer(peer_pp[0])

def common_peer_destroy(self, peer):
	"""Destroy the peer.

	:param rist.Peer peer: peer to be destroyed
	:raises: :class:`rist.ResultException`
	"""

	ResultException.act(self._peer_destroy(self._ptr, peer._ptr))

def common_flow_id_get(self):
	"""Get Flow ID.

	:returns: int
	:raises: :class:`rist.ResultException`
	"""

	val = ffi.new("uint32_t *")
	ResultException.act(self._flow_id_get(self._ptr, val))
	return val[0]

def common_oob_write(self, peer, payload, ts_ntp=0):
	"""Send Out Of Band data.

	:raises: :class:`rist.ResultException`
	"""

	payload = bytes(payload)
	block = ffi.new("struct rist_oob_block *", {
		'peer': peer._ptr,
		'payload': payload,
		'payload_len': len(payload),
		'ts_ntp': ts_ntp
	})

	ResultException.act(self._oob_write(self._ptr, block))

def common_oob_read(self):
	"""Read received Out Of Band data.

	:returns: rist.OobBlock
	:raises: :class:`rist.ResultException`
	"""

	ptr_ptr = ffi.new("struct rist_oob_block **")
	ResultException.act(self._oob_read(self._ptr, ptr_ptr))
	return OobBlock(ptr_ptr[0])

def common_oob_callback_set(self, cb):
	"""Set Out Of Band callback.

	:param cb: Callback (pass *None* to disable)
	:raises: :class:`rist.ResultException`
	"""

	h = ffi.NULL if cb is None else ffi.new_handle(self)
	_cb = ffi.NULL if cb is None else librist.glue_oob_callback
	ResultException.act(self._oob_callback_set(self._ptr, _cb, h))
	self._oob_callback = cb
