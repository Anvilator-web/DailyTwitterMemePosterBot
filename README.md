# Daily Twitter Meme Poster Bot 🤖

This is a python bot which receives memes from Reddit and tweets them to Twitter (UNDER DEVELOPMENT)

Created by [Ketan Chowdhury](https://github.com/anvilator-web)

## Requirements to Run

- A computer running Windows, macOS, Linux, etc
- Python 3.9+
- Dependencies (Listed below in Installation procedure)

## Installation 👩‍💻

1. Install git on your computer:
   - On PC: go to [GIT](https://git-scm.com/download/win), download and install for your computer
   - On Mac: get Homebrew and run `brew install git` in your terminal
   - On Linux: run `sudo apt install git`

2. Clone this repository:
3. Open Terminal or Console and run `pip install rich praw tweepy python-dotenv playwright pandas datetime`
4. Run `playwright install`
5. Rename .env.template to .env
6. Go to [the Reddit Apps Page](https://reddit.com/prefs/apps/) and create a new app as a script.
7. Copy and paste the API Key and Secret to the .env file
8. Go to [the Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
9. Create an App with Essential Access
10. Apply for Elevated Access
11. Wait
12. Get your OAuth 1.0a and OAuth 2.0 turned on and get all the values written to the .env file
13. Go to your favourite subreddit (such as r/memes) and selected some threads which have static images in them
14. Copy link address by right clicking on the image and copying the Link
15. Go to the .env file and paste 5 such meme links
16. And you're set up! (not really you just get 5 images and nothing else)


## Usage

Since this is still in development (indev), you won't be able to upload the meme images to twitter. Also, you have to provide the meme images so it isn't really "automated". So, this is just a basic codebase.


## Contribute!

If you would like to help create open source software at a beginner level and want to contribute to this project, you're more than welcome to!
Clone the project and switch to dev branch, and contribute!
Create a pull request and I'll check out your suggestions

Also, if you want to help create better documentation,
the steps are same but instead of modifying the code files, modify the documentation
