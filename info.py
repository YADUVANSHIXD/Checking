import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '29728878'))
API_HASH = environ.get('API_HASH', 'a961168f7807061e77e1fb39c3f6ef71')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5294914915 7986684117').split()]
USERNAME = environ.get('USERNAME', "https://t.me/B4UOwnerBot") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002179479692'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/B4UMOVIEZONE')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002150820537 -1002235533210').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002470952565'))  # set shortner log channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002224752949')) # The movie you upload in it will be deleted from the bot.
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002471108414'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002041612661'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002478884839') # If anyone sends a request message to your bot, you will get it in this channel.
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002296473971')) # 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/YaduvanshiXsupport') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How_to_open_movielink/17")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/How_to_open_movielink/22")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/How_to_open_movielink/18")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "4030dd8b87e40fb381a15ce48c4a56555bed524e")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'arlinks.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "c4fea41840e9405644de2572c5312a19a9e41286")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'youlinks.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "8a77b545e2c06c440d30e7dedccd234edd74ea34")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'IndiaearnX.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2025 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://te.legra.ph/file/b4a3747fc57c0a78b8ce7.jpg https://te.legra.ph/file/96bfa2b897869b53f3c1b.jpg https://telegra.ph/file/ab7c45feabcd446799ec9.jpg https://telegra.ph/file/be0e05a69125057f7403d.jpg https://telegra.ph/file/083d98858adfc45ce1761.jpg https://telegra.ph/file/c3e7e855f6fe2deb7fe21.jpg https://telegra.ph/file/966dae7b6f91a58aa037c.jpg https://telegra.ph/file/fa74ca254cc4368c167cd.jpg https://telegra.ph/file/08e2e68f2d9c959ca30fc.jpg https://telegra.ph/file/1d63c8f8102d8bf6dd90f.jpg https://envs.sh/Wza.jpg https://files.catbox.moe/kf2c2z.jpg https://files.catbox.moe/tljzgo.jpg https://files.catbox.moe/gtonu2.jpg https://files.catbox.moe/4az6sz.jpg https://files.catbox.moe/ceg0l0.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/WzX.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://envs.sh/WzO.jpg'))
REACTIONS = ["👀", "😈", "🔥", "😍", "🎉", "🥰", "❤️", "🤠", "😘", "🙏", "🤗", "😻", "🌹", "👻", "🌚", "🤡", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '21600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'True')), False)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', False) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1800))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'tutorial_2': TUTORIAL_2,
            'tutorial_3': TUTORIAL_3,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
