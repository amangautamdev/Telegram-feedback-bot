import os
from os import environ
from os import getenv

class Config(object):
	APP_ID = int(os.environ.get("APP_ID", "26945844"))
	API_HASH = os.environ.get("API_HASH", "9f2f1d81fd2af2b21a700fa6681215b1")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7112282983:AAFS1ji7qHjB7vozFwK8IN5KGfqWKXK_bMA")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	BOT_OWNER = int(os.environ.get("5631563685"))
	SESSION_STRING = environ.get("SESSION_STRING", None)
	OWNER = list(map(int, getenv("OWNER").split())) # ain karanna epa hehe
	MONGODB_URI = os.environ.get("MONGODB_URI")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY"))
	ARQ_API_KEY = os.environ.get("ARQ_API_KEY")

