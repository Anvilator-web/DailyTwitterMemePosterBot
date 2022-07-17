import os
import rich
import praw
import tweepy
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
from sleep import *
from playwright.sync_api import sync_playwright

version = 0.1
load_dotenv()

rich.print("Daily[bold cyan]Twitter[/bold cyan]MemePosterBot")
rich.print("[red]version[/red]", version)

sleep_1()

rich.print('|--------------------------------------------------------------------|')
rich.print('|Checking .env file for API Keys...                                  |')
rich.print('|____________________________________________________________________|')

# Loading Twitter API Keys
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_TOKEN_SECRET = os.getenv("TWITTER_TOKEN_SECRET")

# Loading Reddit API Keys
REDDIT_API_KEY = os.getenv("REDDIT_API_KEY")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_APP_NAME = os.getenv("REDDIT_APP_NAME")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_MEME_1_LINK = os.getenv("REDDIT_MEME_1_LINK")
REDDIT_MEME_2_LINK = os.getenv("REDDIT_MEME_2_LINK")
REDDIT_MEME_3_LINK = os.getenv("REDDIT_MEME_3_LINK")
REDDIT_MEME_4_LINK = os.getenv("REDDIT_MEME_4_LINK")
REDDIT_MEME_5_LINK = os.getenv("REDDIT_MEME_5_LINK")


sleep_1()

if  TWITTER_API_KEY == "":
    rich.print("❗ [bold cyan]Twitter[/bold cyan] [bold red]API Key is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the API Key")
    TWITTER_API_KEY_EXISTS = "false"
else:
    TWITTER_API_KEY_EXISTS = "true"

if TWITTER_API_SECRET == "":
    rich.print("❗ [bold cyan]Twitter[/bold cyan] [bold red]API Secret is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the API Secret")
    TWITTER_API_SECRET_EXISTS = "false"
else:
    TWITTER_API_SECRET_EXISTS = "true"

if TWITTER_BEARER_TOKEN == "":
    rich.print("❗ [bold cyan]Twitter[/bold cyan] [bold red]Bearer Token is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the Bearer Token")
    TWITTER_BEARER_TOKEN_EXISTS = "false"
else:
    TWITTER_BEARER_TOKEN_EXISTS = "true"

if  TWITTER_ACCESS_TOKEN == "":
    rich.print("❗ [bold cyan]Twitter[/bold cyan] [bold red]Access Token is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the Access Token")
    TWITTER_ACCESS_TOKEN_EXISTS = "false"
else:
    TWITTER_ACCESS_TOKEN_EXISTS = "true"

if  TWITTER_TOKEN_SECRET == "":
    rich.print("❗ [bold cyan]Twitter[/bold cyan] [bold red]Token Secret is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the Token Secret")
    TWITTER_TOKEN_SECRET_EXISTS = "false"
else:
    TWITTER_TOKEN_SECRET_EXISTS = "true"

if REDDIT_API_KEY == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]API Key is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the API Key")
    REDDIT_API_KEY_EXISTS = "false"
else:
    REDDIT_API_KEY_EXISTS = "true"

if REDDIT_SECRET == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Secret is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the Secret")
    REDDIT_SECRET_EXISTS = "false"
else:
    REDDIT_SECRET_EXISTS = "true"

if REDDIT_APP_NAME == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]App Name is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the App Name")
    REDDIT_APP_NAME_EXISTS = "false"
else:
    REDDIT_APP_NAME_EXISTS = "true"

if REDDIT_USERNAME == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Username is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered your username")
    REDDIT_USERNAME_EXISTS = "false"
else:
    REDDIT_USERNAME_EXISTS = "true"

if REDDIT_PASSWORD == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Password is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered your password")
    REDDIT_PASSWORD_EXISTS = "false"
else:
    REDDIT_PASSWORD_EXISTS = "true"

if REDDIT_MEME_1_LINK == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Meme 1 Link is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the link of Meme 1")
    REDDIT_MEME_1_LINK_EXISTS = "false"
else:
    REDDIT_MEME_1_LINK_EXISTS = "true"

if REDDIT_MEME_2_LINK == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Meme 2 Link is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the link of Meme 2")
    REDDIT_MEME_2_LINK_EXISTS = "false"
else:
    REDDIT_MEME_2_LINK_EXISTS = "true"

if REDDIT_MEME_3_LINK == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Meme 3 Link is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the link of Meme 3")
    REDDIT_MEME_3_LINK_EXISTS = "false"
else:
    REDDIT_MEME_3_LINK_EXISTS = "true"

if REDDIT_MEME_4_LINK == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Meme 4 Link is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the link of Meme 4")
    REDDIT_MEME_4_LINK_EXISTS = "false"
else:
    REDDIT_MEME_4_LINK_EXISTS = "true"

if REDDIT_MEME_5_LINK == "":
    rich.print("❗ [bold orange3]Reddit[/bold orange3] [bold red]Meme 5 Link is not provided in .env file[/bold red]")
    rich.print("Check .env file if you have entered the link of Meme 5")
    REDDIT_MEME_5_LINK_EXISTS = "false"
else:
    REDDIT_MEME_5_LINK_EXISTS = "true"



if TWITTER_API_KEY_EXISTS == "false" and TWITTER_API_SECRET_EXISTS == "false" and TWITTER_BEARER_TOKEN_EXISTS == "false" and REDDIT_API_KEY_EXISTS == "false" and REDDIT_SECRET_EXISTS == "false" and REDDIT_APP_NAME_EXISTS == "false" and REDDIT_USERNAME_EXISTS == "false" and REDDIT_PASSWORD_EXISTS == "false" and REDDIT_MEME_1_LINK_EXISTS == "false" and REDDIT_MEME_2_LINK_EXISTS == "false" and REDDIT_MEME_3_LINK_EXISTS == "false"  and REDDIT_MEME_4_LINK_EXISTS == "false" and REDDIT_MEME_5_LINK_EXISTS == "false" and TWITTER_ACCESS_TOKEN_EXISTS == "false" and TWITTER_TOKEN_SECRET == "false":
    rich.print("❗ API Keys are not provided in the .env file")
    rich.print("Check .env file and enter values before running main.py")
    rich.print("[bold red]Exiting...[/bold red]")
    exit()
elif TWITTER_API_KEY_EXISTS == "true" and TWITTER_API_SECRET_EXISTS == "true" and TWITTER_BEARER_TOKEN_EXISTS == "true" and REDDIT_API_KEY_EXISTS == "true" and REDDIT_SECRET_EXISTS == "true" and REDDIT_APP_NAME_EXISTS == "true" and REDDIT_USERNAME_EXISTS == "true" and REDDIT_PASSWORD_EXISTS == "true" and REDDIT_MEME_1_LINK_EXISTS == "true" and REDDIT_MEME_2_LINK_EXISTS == "true" and REDDIT_MEME_3_LINK_EXISTS == "true"  and REDDIT_MEME_4_LINK_EXISTS == "true" and REDDIT_MEME_5_LINK_EXISTS == "true" and TWITTER_ACCESS_TOKEN_EXISTS == "true" and TWITTER_TOKEN_SECRET_EXISTS == "true":
    rich.print('|--------------------------------------------------------------------|')
    rich.print('|[green]API Keys loaded ✔[/green]️                                                   |')
    rich.print('|____________________________________________________________________|')

# Now, for the reddit part of the program

# playwright download memes

with sync_playwright() as p:
    rich.print("Launching browser...")
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(REDDIT_MEME_1_LINK)
    page.screenshot(path="reddit_meme_1.png")
    browser.close()

with sync_playwright() as p:
    rich.print("Launching browser...")
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page =  browser.new_page()
    page.goto(REDDIT_MEME_2_LINK)
    page.screenshot(path="reddit_meme_2.png")
    browser.close()

with sync_playwright() as p:
    rich.print("Launching browser...")
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page =  browser.new_page()
    page.goto(REDDIT_MEME_3_LINK)
    page.screenshot(path="reddit_meme_3.png")
    browser.close()

with sync_playwright() as p:
    rich.print("Launching browser...")
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page =  browser.new_page()
    page.goto(REDDIT_MEME_4_LINK)
    page.screenshot(path="reddit_meme_4.png")
    browser.close()

with sync_playwright() as p:
    rich.print("Launching browser...")
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page =  browser.new_page()
    page.goto(REDDIT_MEME_5_LINK)
    page.screenshot(path="reddit_meme_5.png")
    browser.close()


# Now, for the twitter part of the program

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(status = "")
