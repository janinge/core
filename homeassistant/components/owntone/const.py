"""Const for owntone."""
from homeassistant.components.media_player.const import (
    SUPPORT_BROWSE_MEDIA,
    SUPPORT_CLEAR_PLAYLIST,
    SUPPORT_NEXT_TRACK,
    SUPPORT_PAUSE,
    SUPPORT_PLAY,
    SUPPORT_PLAY_MEDIA,
    SUPPORT_PREVIOUS_TRACK,
    SUPPORT_SEEK,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_SHUFFLE_SET,
    SUPPORT_STOP,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_VOLUME_SET, MEDIA_CLASS_DIRECTORY, MEDIA_CLASS_PLAYLIST, MEDIA_TYPE_PLAYLIST, MEDIA_CLASS_ARTIST,
    MEDIA_TYPE_ARTIST, MEDIA_CLASS_ALBUM, MEDIA_TYPE_ALBUM, MEDIA_TYPE_GENRE, MEDIA_CLASS_GENRE, MEDIA_CLASS_PODCAST,
    MEDIA_TYPE_PODCAST, MEDIA_CLASS_CHANNEL, MEDIA_TYPE_CHANNELS,
)

CALLBACK_TIMEOUT = 8  # max time between command and callback from owntone server
CONF_LIBRESPOT_JAVA_PORT = "librespot_java_port"
CONF_MAX_PLAYLISTS = "max_playlists"
CONF_TTS_PAUSE_TIME = "tts_pause_time"
CONF_TTS_VOLUME = "tts_volume"
DEFAULT_PORT = 3689
DEFAULT_SERVER_NAME = "My Server"
DEFAULT_TTS_PAUSE_TIME = 1.2
DEFAULT_TTS_VOLUME = 0.8
DEFAULT_UNMUTE_VOLUME = 0.6
DOMAIN = "owntone"  # key for hass.data
FD_NAME = "owntone"
HASS_DATA_REMOVE_LISTENERS_KEY = "REMOVE_LISTENERS"
HASS_DATA_UPDATER_KEY = "UPDATER"
KNOWN_PIPES = {"librespot-java"}
LIBRARY_MAP = {
    "playlists": dict(title="Playlists", media_class=MEDIA_CLASS_PLAYLIST, media_content_type=MEDIA_TYPE_PLAYLIST),
    "artists": dict(title="Artists", media_class=MEDIA_CLASS_ARTIST, media_content_type=MEDIA_TYPE_ARTIST),
    "albums": dict(title="Albums", media_class=MEDIA_CLASS_ALBUM, media_content_type=MEDIA_TYPE_ALBUM),
    "genres": dict(title="Genres", media_class=MEDIA_CLASS_GENRE, media_content_type=MEDIA_TYPE_GENRE),
    "podcasts": dict(title="Podcasts", media_class=MEDIA_CLASS_PODCAST, media_content_type=MEDIA_TYPE_PODCAST),
    "radio": dict(title="Radio", media_class=MEDIA_CLASS_CHANNEL, media_content_type=MEDIA_TYPE_CHANNELS),
}
PIPE_FUNCTION_MAP = {
    "librespot-java": {
        "async_media_play": "player_resume",
        "async_media_pause": "player_pause",
        "async_media_stop": "player_pause",
        "async_media_previous_track": "player_prev",
        "async_media_next_track": "player_next",
    }
}
SIGNAL_ADD_ZONES = "owntone_add_zones {}"
SIGNAL_CONFIG_OPTIONS_UPDATE = "owntone_config_options_update {}"
SIGNAL_UPDATE_DATABASE = "owntone_update_database {}"
SIGNAL_UPDATE_MASTER = "owntone_update_master {}"
SIGNAL_UPDATE_OUTPUTS = "owntone_update_outputs {}"
SIGNAL_UPDATE_PLAYER = "owntone_update_player {}"
SIGNAL_UPDATE_QUEUE = "owntone_update_queue {}"
SOURCE_NAME_CLEAR = "Clear queue"
SOURCE_NAME_DEFAULT = "Default (no pipe)"
STARTUP_DATA = {
    "player": {
        "state": "stop",
        "repeat": "off",
        "consume": False,
        "shuffle": False,
        "volume": 0,
        "item_id": 0,
        "item_length_ms": 0,
        "item_progress_ms": 0,
    },
    "queue": {"version": 0, "count": 0, "items": []},
    "outputs": [],
}
SUPPORTED_FEATURES = (
    SUPPORT_PLAY
    | SUPPORT_PAUSE
    | SUPPORT_STOP
    | SUPPORT_SEEK
    | SUPPORT_VOLUME_SET
    | SUPPORT_VOLUME_MUTE
    | SUPPORT_PREVIOUS_TRACK
    | SUPPORT_NEXT_TRACK
    | SUPPORT_CLEAR_PLAYLIST
    | SUPPORT_SELECT_SOURCE
    | SUPPORT_SHUFFLE_SET
    | SUPPORT_TURN_ON
    | SUPPORT_TURN_OFF
    | SUPPORT_PLAY_MEDIA
    | SUPPORT_BROWSE_MEDIA
)
SUPPORTED_FEATURES_ZONE = (
    SUPPORT_VOLUME_SET | SUPPORT_VOLUME_MUTE | SUPPORT_TURN_ON | SUPPORT_TURN_OFF
)
TTS_TIMEOUT = 20  # max time to wait between TTS getting sent and starting to play
