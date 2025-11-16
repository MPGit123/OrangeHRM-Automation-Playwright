from utils.env_loader import load_env_file
import os

load_env_file()

class Settings():
    browser: str = os.getenv("BROWSER")
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    default_timeout_ms: int = int(os.getenv("DEFAULT_TIMEOUT_MS"))
    slow_mo_ms: int = int(os.getenv("SLOW_MO_MS"))
    base_url: str = os.getenv("BASE_URL")
    username: str = os.getenv("USER_ID")
    password: str = os.getenv("PASSWORD")

settings = Settings()