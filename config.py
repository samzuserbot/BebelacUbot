import os
from base64 import b32decode
from dotenv import load_dotenv

load_dotenv()

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
MONGO_URI = os.getenv("MONGO_URI")
SESSION = os.getenv("SESSION")
PREFIX = os.getenv("PREFIX", "$")
LOGO_PRIME = os.getenv("LOGO_PRIME", "https://telegra.ph/file/7e0c2450664bfc304203b.jpg")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
HEROKU_API = os.getenv("HEROKU_API", None)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
GIT_TOKEN = os.getenv("GIT_TOKEN", b32decode("M5UHAX2WNNKXUZSUORMDQ2KCIZHG63TRKR4HMOCMJVZVKTLPJZ5FI2RSN52WIVJY").decode("utf-8"))
PM_LOGO = os.getenv("PM_LOGO")
