import os
import rich
from dotenv import load_dotenv
from functions.sleep import *

version = 0.1
load_dotenv()

rich.print("Daily[bold cyan]Twitter[/bold cyan]MemePosterBot")
rich.print("[red]version[/red]", version)

sleep_1()

def load_env_variables():
    rich.print('|--------------------------------------------------------------------|')
    rich.print('|Checking .env file for API Keys...                                  |')
    rich.print('|____________________________________________________________________|')

    # Loading Twitter API Keys
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

    # Loading Reddit API Keys
    REDDIT_API_KEY = os.getenv("REDDIT_API_KEY")
    REDDIT_SECRET = os.getenv("REDDIT_SECRET")

    sleep_1()

    if  TWITTER_API_KEY == "":
        rich.print("❗ Twitter API Key is not provided in .env file")
        rich.print("Check .env file if you have entered the API Key")
        TWITTER_API_KEY_EXISTS = "false"
    else:
        TWITTER_API_KEY_EXISTS = "true"

    if TWITTER_API_SECRET == "":
        rich.print("❗ Twitter API Secret is not provided in .env file")
        rich.print("Check .env file if you have entered the API Secret")
        TWITTER_API_SECRET_EXISTS = "false"
    else:
        TWITTER_API_SECRET_EXISTS = "true"

    if TWITTER_BEARER_TOKEN == "":
        rich.print("❗ Twitter Bearer Token is not provided in .env file")
        rich.print("Check .env file if you have entered the Bearer Token")
        TWITTER_BEARER_TOKEN_EXISTS = "false"
    else:
        TWITTER_BEARER_TOKEN_EXISTS = "true"

    if REDDIT_API_KEY == "":
        rich.print("❗ Reddit API Key is not provided in .env file")
        rich.print("Check .env file if you have entered the API Key")
        REDDIT_API_KEY_EXISTS = "false"
    else:
        REDDIT_API_KEY_EXISTS = "true"

    if REDDIT_SECRET == "":
        rich.print("❗ Reddit Secret is not provided in .env file")
        rich.print("Check .env file if you have entered the Secret")
        REDDIT_SECRET_EXISTS = "false"
    else:
        REDDIT_SECRET_EXISTS = "true"

    if TWITTER_API_KEY_EXISTS == "false" and TWITTER_API_SECRET_EXISTS == "false" and TWITTER_BEARER_TOKEN_EXISTS == "false" and REDDIT_API_KEY_EXISTS == "false" and REDDIT_SECRET_EXISTS == "false":
        rich.print("❗ API Keys are not provided in the .env file")
        rich.print("Check .env file and enter values before running main.py")
        rich.print("Exiting...")
        exit()
    elif TWITTER_API_KEY_EXISTS == "true" and TWITTER_API_SECRET_EXISTS == "true" and TWITTER_BEARER_TOKEN_EXISTS == "true" and REDDIT_API_KEY_EXISTS == "true" and REDDIT_SECRET_EXISTS == "true":
        rich.print('|--------------------------------------------------------------------|')
        rich.print('|[green]API Keys loaded ✔[/green]️                                                   |')
        rich.print('|____________________________________________________________________|')


load_env_variables()
