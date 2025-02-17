import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Adzuna API Credentials
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

# Database URL
DB_URL = os.getenv("DB_URL")

# Logging Level
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Number of pages to scrape
SCRAPE_NUM_PAGES = int(os.getenv("SCRAPE_NUM_PAGES", 1))

# Verify the environment variables (Optional)
if __name__ == "__main__":
    print(f"APP_ID: {APP_ID}")
    print(f"APP_KEY: {APP_KEY}")
    print(f"DB_URL: {DB_URL}")
    print(f"LOG_LEVEL: {LOG_LEVEL}")
    print(f"SCRAPE_NUM_PAGES: {SCRAPE_NUM_PAGES}")
