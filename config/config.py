import os
from pathlib import Path
from dotenv import load_dotenv

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / ".env")

SNOWFLAKE_ACCOUNT: str | None = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_ACCOLNIT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER= os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")

SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
SNOWFLAKE_ROLE = os.getenv("SNOWFLAKE_ROLE")