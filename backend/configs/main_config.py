import os
from dotenv import load_dotenv

load_dotenv()

APP_CONFIG = {
    "host": "0.0.0.0",
    "port": 8080,
    "debug": True,
}

DATABASE_PATH = os.getenv("DATABASE_NAME", "")
API_PREFIX = "api"
API_VERSION = "v1"
