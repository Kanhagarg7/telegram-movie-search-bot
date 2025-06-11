import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ.get('API_ID', '6'))
API_HASH = environ.get('API_HASH', 'eb06d4abfb49dc3eeb1aeb98ae0f581e')
BOT_TOKEN = environ.get('BOT_TOKEN', "7510817339:AAHFZoFzPkUO_-nAwfh9bjY_qHsWMprM2PI")

USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = 5873900195
CHANNELS = -1002851899064
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://kanhagarg930123:kanha@kanha.jhlzb3k.mongodb.net/?retryWrites=true&w=majority&appName=kanha")

DATABASE_NAME = environ.get('DATABASE_NAME', "kanha")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
