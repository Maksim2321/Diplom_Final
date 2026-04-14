import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL: str = os.getenv("BASE_URL")
API_URL: str = os.getenv("API_URL")
API_KEY: str = os.getenv("API_KEY")
