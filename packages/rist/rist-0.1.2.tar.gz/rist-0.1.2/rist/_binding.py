# pyRIST. Copyright 2019-2020 Mad Resistor LLP. All right reserved.
# Author: Kuldeep Singh Dhaka <kuldeep@madresistor.com>

import sys
import cffi

ffi = cffi.FFI()

ffi.cdef("""
	/* Used for cname, miface and shared secret */
	#define RIST_MAX_STRING_SHORT 128
	/* Used for url/address */
	#define RIST_MAX_STRING_LONG 256

	/* Track PROTOCOL and API changes */
	#define RIST_PROTOCOL_VERSION 2
	#define RIST_API_VERSION 6
	#define RIST_SUBVERSION 5
	#define RIST_PEER_CONFIG_VERSION 0

	/* Default peer config values */
	#define RIST_DEFAULT_VIRT_SRC_PORT 1971
	#define RIST_DEFAULT_VIRT_DST_PORT 1968
	/* #define RIST_DEFAULT_RECOVERY_MODE RIST_RECOVERY_MODE_TIME */
	#define RIST_DEFAULT_RECOVERY_MAXBITRATE 100000
	#define RIST_DEFAULT_RECOVERY_MAXBITRATE_RETURN 0
	#define RIST_DEFAULT_RECOVERY_LENGHT_MIN 1000
	#define RIST_DEFAULT_RECOVERY_LENGHT_MAX 1000
	#define RIST_DEFAULT_RECOVERY_REORDER_BUFFER 25
	#define RIST_DEFAULT_RECOVERY_RTT_MIN 50
	#define RIST_DEFAULT_RECOVERY_RTT_MAX 500
	/* #define RIST_DEFAULT_BUFFER_BLOAT_MODE RIST_BUFFER_BLOAT_MODE_OFF */
	#define RIST_DEFAULT_BUFFER_BLOAT_LIMIT	6
	#define RIST_DEFAULT_BUFFER_BLOAT_HARD_LIMIT 20
	/* #define RIST_DEFAULT_VERBOSE_LEVEL RIST_LOG_WARN */
	/* #define RIST_DEFAULT_PROFILE RIST_PROFILE_MAIN */
	#define RIST_DEFAULT_SESSION_TIMEOUT 60000
	#define RIST_DEFAULT_KEEPALIVE_INTERVAL 1000

	/* Rist URL parameter names (per peer) */
	/* #define RIST_URL_PARAM_BUFFER_SIZE     "buffer" */
	/* #define RIST_URL_PARAM_SECRET          "secret" */
	/* #define RIST_URL_PARAM_AES_TYPE        "aes-type" */
	/* #define RIST_URL_PARAM_BANDWIDTH       "bandwidth" */
	/* #define RIST_URL_PARAM_RET_BANDWIDTH   "return-bandwidth" */
	/* #define RIST_URL_PARAM_REORDER_BUFFER  "reorder-buffer" */
	/* #define RIST_URL_PARAM_RTT             "rtt" */
	/* #define RIST_URL_PARAM_COMPRESSION     "compression" */
	/* #define RIST_URL_PARAM_CNAME           "cname" */
	/* #define RIST_URL_PARAM_VIRT_DST_PORT   "virt-dst-port" */
	/* #define RIST_URL_PARAM_WEIGHT          "weight" */
	/* #define RIST_URL_PARAM_MIFACE          "miface" */
	/* #define RIST_URL_PARAM_SESSION_TIMEOUT "session-timeout" */
	/* #define RIST_URL_PARAM_KEEPALIVE_INT   "keepalive-interval" */
	/* Rist additional parameter names */
	/* #define RIST_URL_PARAM_VIRT_SRC_PORT   "virt-src-port" */
	/* #define RIST_URL_PARAM_PROFILE         "profile" */
	/* #define RIST_URL_PARAM_VERBOSE_LEVEL   "verbose-level" */

	enum rist_nack_type {
		RIST_NACK_RANGE = 0,
		RIST_NACK_BITMASK = 1,
	};

	enum rist_profile {
		RIST_PROFILE_SIMPLE = 0,
		RIST_PROFILE_MAIN = 1,
		RIST_PROFILE_ADVANCED = 2,
	};

	enum rist_log_level {
		RIST_LOG_QUIET = -1,
		RIST_LOG_INFO = 0,
		RIST_LOG_ERROR = 1,
		RIST_LOG_WARN = 2,
		RIST_LOG_DEBUG = 3,
		RIST_LOG_SIMULATE = 4,
	};

	enum rist_recovery_mode {
		RIST_RECOVERY_MODE_UNCONFIGURED = 0,
		RIST_RECOVERY_MODE_DISABLED = 1,
		RIST_RECOVERY_MODE_BYTES = 2,
		RIST_RECOVERY_MODE_TIME = 3,
	};

	enum rist_buffer_bloat_mode {
		RIST_BUFFER_BLOAT_MODE_OFF = 0,
		RIST_BUFFER_BLOAT_MODE_NORMAL = 1,
		RIST_BUFFER_BLOAT_MODE_AGGRESSIVE = 2
	};

	enum rist_data_block_flags {
		RIST_DATA_FLAGS_USE_SEQ = 1,
		RIST_DATA_FLAGS_NEED_FREE = 2,
	};

	struct rist_receiver;
	struct rist_sender;
	struct rist_peer;

	struct rist_data_block {
		const void *payload;
		size_t payload_len;
		uint64_t ts_ntp;
		/* The virtual source and destination ports are not used for simple profile */
		uint16_t virt_src_port;
		/* These next fields are not needed/used by rist_sender_data_write */
		uint16_t virt_dst_port;
		struct rist_peer *peer;
		uint32_t flow_id;
		/* Get's populated by librist with the rtp_seq on output, can be used on input to tell librist which rtp_seq to use */
		uint64_t seq;
		uint32_t flags;
	};

	struct rist_oob_block {
		struct rist_peer *peer;
		const void *payload;
		size_t payload_len;
		uint64_t ts_ntp;
	};

	struct rist_peer_config {
		int version;

		/* Communication parameters */
		// If a value of 0 is specified for address family, the library
		// will parse the address and populate all communication parameters.
		// Alternatively, use either AF_INET or AF_INET6 and address will be
		// treated like an IP address or hostname
		int address_family;
		int initiate_conn;
		const char address[RIST_MAX_STRING_LONG];
		const char miface[RIST_MAX_STRING_SHORT];
		uint16_t physical_port;

		/* The virtual destination port is not used for simple profile */
		uint16_t virt_dst_port;

		/* Recovery options */
		enum rist_recovery_mode recovery_mode;
		uint32_t recovery_maxbitrate;
		uint32_t recovery_maxbitrate_return;
		uint32_t recovery_length_min;
		uint32_t recovery_length_max;
		uint32_t recovery_reorder_buffer;
		uint32_t recovery_rtt_min;
		uint32_t recovery_rtt_max;

		/* Load balancing weight (use 0 for duplication) */
		uint32_t weight;

		/* Encryption */
		const char secret[RIST_MAX_STRING_SHORT];
		int key_size;
		uint32_t key_rotation;

		/* Compression (sender only as receiver is auto detect) */
		int compression;

		/* cname identifier for rtcp packets */
		const char cname[RIST_MAX_STRING_SHORT];

		/* Congestion control */
		enum rist_buffer_bloat_mode buffer_bloat_mode;
		uint32_t buffer_bloat_limit;
		uint32_t buffer_bloat_hard_limit;

		/* Connection options */
		uint32_t session_timeout;
		uint32_t keepalive_interval;

	};
	int rist_sender_create(struct rist_sender **ctx, enum rist_profile profile,
					uint32_t flow_id, enum rist_log_level log_level);
	int rist_sender_auth_handler_set(struct rist_sender *ctx,
			int (*connect_cb)(void *arg, const char* conn_ip, uint16_t conn_port,
					const char* local_ip, uint16_t local_port, struct rist_peer *peer),
			int (*disconn_cb)(void *arg, struct rist_peer *peer),
			void *arg);
	int rist_sender_peer_create(struct rist_sender *ctx,
			struct rist_peer **peer, const struct rist_peer_config *config);
	int rist_sender_peer_destroy(struct rist_sender *ctx,
			struct rist_peer *peer);
	int rist_sender_jitter_max_set(struct rist_sender *ctx, int t);
	int rist_sender_oob_callback_set(struct rist_sender *ctx,
			int (*oob_callback)(void *arg, const struct rist_oob_block *oob_block),
			void *arg);
	int rist_sender_start(struct rist_sender *ctx);
	int rist_sender_oob_write(struct rist_sender *ctx, const struct rist_oob_block *oob_block);
	int rist_sender_oob_read(struct rist_sender *ctx, const struct rist_oob_block **oob_block);
	int rist_sender_data_write(struct rist_sender *ctx, const struct rist_data_block *data_block);
	int rist_sender_destroy(struct rist_sender *ctx);
	int rist_sender_flow_id_get(struct rist_sender *ctx, uint32_t *flow_id);
	int rist_sender_flow_id_set(struct rist_sender *ctx, uint32_t flow_id);
	int rist_receiver_create(struct rist_receiver **ctx, enum rist_profile profile,
				enum rist_log_level log_level);
	int rist_receiver_auth_handler_set(struct rist_receiver *ctx,
			int (*connect_cb)(void *arg, const char* conn_ip, uint16_t conn_port,
					const char* local_ip, uint16_t local_port, struct rist_peer *peer),
			int (*disconn_cb)(void *arg, struct rist_peer *peer),
			void *arg);
	int rist_receiver_peer_create(struct rist_receiver *ctx,
			struct rist_peer **peer, const struct rist_peer_config *config);
	int rist_receiver_peer_destroy(struct rist_receiver *ctx,
			struct rist_peer *peer);
	int rist_receiver_jitter_max_set(struct rist_receiver *ctx, int t);
	int rist_receiver_oob_callback_set(struct rist_receiver *ctx,
			int (*oob_callback)(void *arg, const struct rist_oob_block *oob_block),
			void *arg);
	int rist_receiver_nack_type_set(struct rist_receiver *ctx, enum rist_nack_type nacks_type);
	int rist_receiver_data_callback_set(struct rist_receiver *ctx,
		int (*data_callback)(void *arg, const struct rist_data_block *data_block),
		void *arg);
	int rist_receiver_start(struct rist_receiver *ctx);
	int rist_receiver_oob_write(struct rist_receiver *ctx, const struct rist_oob_block *oob_block);
	int rist_receiver_oob_read(struct rist_receiver *ctx, const struct rist_oob_block **oob_block);
	int rist_receiver_data_read(struct rist_receiver *ctx, const struct rist_data_block **data_block, int timeout);
	int rist_receiver_destroy(struct rist_receiver *ctx);
	int rist_parse_address(const char *url, const struct rist_peer_config **peer_config);
""")

# https://bitbucket.org/cffi/cffi/issues/219
ext = "so" if sys.platform != "win32" else "dll"
librist = ffi.dlopen("librist." + ext)
