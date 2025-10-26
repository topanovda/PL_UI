import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:
    if os.environ["STAGE"] == "dev":
        LOGIN = os.getenv("DEV_LOGIN")
        PASSWORD = os.getenv("DEV_PASSWORD")

    elif os.environ["STAGE"] == "staging":
        LOGIN = os.getenv("STAGING_LOGIN")
        PASSWORD = os.getenv("STAGING_PASSWORD")

    elif os.environ["STAGE"] == "production":
        LOGIN = os.getenv("PROD_LOGIN")
        PASSWORD = os.getenv("PROD_PASSWORD")