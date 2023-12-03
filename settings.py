import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

if DISCORD_API_SECRET is None:
    raise ValueError("DISCORD_API_TOKEN is not set in the environment.")