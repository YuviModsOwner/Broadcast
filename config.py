import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7667830628:AAG3MFhzm3QL8RkcBzZOtRKbhifB4TKzjpw")
API_ID = int(os.environ.get("API_ID", "23718025"))
API_HASH = os.environ.get("API_HASH", "9406106ce28ea71dd12d8cdad937e535")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002234809125"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5495601013").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://gamerspo56:<db_password>@yuvi.2uc3u.mongodb.net/?retryWrites=true&w=majority&appName=Yuvi")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
