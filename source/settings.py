from os import environ
from dotenv import load_dotenv

load_dotenv()

URL_TOR_BROWSER = environ.get("URL_TOR_BROWSER")
FILE_TOR_BROWSER = environ.get("FILE_TOR_BROWSER")
URL_API = environ.get("URL_API")
