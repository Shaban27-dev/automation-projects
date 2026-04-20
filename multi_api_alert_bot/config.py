from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")
RECIPIENT = os.getenv("EMAIL_TO")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TEMP_THRESHOLD = 35
STOCK_THRESHOLD = 5