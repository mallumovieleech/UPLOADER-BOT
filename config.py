import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7945308877:AAEImD7zmngAKeF554rG0Cqf0sU9R5FD26o")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 23858762))
    API_HASH = os.environ.get("API_HASH", "d4d6e9a9e553759e45f59c2e74c8f809")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "561339410"))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jamiedornankoyyodan:jamiedornankoyyodan@cluster0.ioz6q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER", "BQFsDkoAkHUUZ0VYWv2zbVS03LrzePXg5U0mpwaIbXZQdXJhjHuDZVNz6X6SYVG1xpIYXm5SPyB8X5TZ45PpJdXEf3HEEhMyeXR5KneaWWQ6ZniX7DjSnE5YHkwR3V90sFC2OcWiuH3qDhr8pUSVkrJE6sGaDrhRZrCFpClPdhpJgpGRRntGwYSvFs4nBYsVb8oCu-avva6ff3-WKB4yV1jkmLHr5rt0QZ38K0sMkDtwbzrY4Dfg57XYWFMNsIp5guusWVKmPoos5FWI_jBQ5cjBLnH3Sa6GIrllxm8j2nS9YDCsINvr2IXLsvXmVZPmuV-4GEkYwO5fN5zC4FKIp-EhZxiJawAAAAHnBYTeAA")
