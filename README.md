# RedditToIG
A script that automatically downloads images from a subreddit and reposts them to Instagram.

Before running, edit the `config.py` file with the required information.

## Requirements

Before you can run this script, you'll need to ensure you have the following Python libraries installed:

- `praw`: The Python Reddit API Wrapper for interacting with Reddit.
- `requests`: A library for making HTTP requests, used for downloading images.
- `instagrapi`: A Python wrapper for the Instagram Private API, used for posting images to Instagram.

You can install these libraries using pip:

```bash
pip install praw requests instagrapi
```

## Usage

Once you have set up the configuration and installed the required libraries, you can run the script to automatically download images from a subreddit and repost them to Instagram.

```bash
python main.py
