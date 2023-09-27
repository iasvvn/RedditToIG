import praw
import requests
import os 
import time 
from instagrapi import Client
import config

folder_path = 'downloaded_images'

def GetMeme(folder_path):
    client_id = config.client_id
    client_secret = config.client_secret
    user_agent = 'RedditToIG'

    reddit = praw.Reddit(
        client_id = client_id,
        client_secret = client_secret,
        password = config.reddit_pass,
        user_agent = user_agent,
        username= config.reddit_username,
    )

    subreddit_name = config.subreddit_name

    num_images = 1

    os.makedirs(folder_path, exist_ok=True)

    #start here

    while True:

        retry_limit = 10  # Number of retries to fetch an image
        retry_count = 0
        downloaded = False

        while retry_count < retry_limit:
            # Fetch hot submissions from the last hour (you can change the time filter)
            submission_generator = reddit.subreddit(subreddit_name).top(time_filter='hour', limit=num_images)

            for submission in submission_generator:
                print(submission.url)

                if submission.url and submission.url.endswith(('.jpg', '.jpeg', '.png')):
                    image_url = submission.url
                    image_filename = os.path.join(folder_path, f'{submission.id}.jpg')

                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(image_filename, 'wb') as f:
                            f.write(response.content)
                        print(f'Downloaded: {image_filename}')
                        downloaded = True
                        retry_count = retry_limit  # Exit the loop once an image is successfully downloaded
                        break
                    else:
                        print(f'Failed to download: {image_url}')

            retry_count += 1

        if not downloaded:
            print(f'No images found after {retry_limit} retries.')
            print(retry_count)
        return image_filename
    
def CleanUp(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
    except Exception as e:
        print(e)
        
        
def Upload():
    client = Client()
    try:
        client.login(config.instagram_username, config.instagram_pass) 
    except Exception as e:
        print(e)
        time.sleep(5)
        exit()
    post = GetMeme(folder_path)
    caption = config.caption_text + '\n\n' + config.hashtags
    try:
        client.photo_upload(post,caption)
    except Exception as e:
        print(e)
    else: 
        print('Posted')
        print('Sleeping...')
    finally:
        CleanUp(folder_path)
    client.logout()
        
while True:
    Upload()
    time.sleep(config.sleep_time)