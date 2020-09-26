import praw
import os

r = praw.Reddit(
    client_id='9sMbfS0kHaVZlQ',
    client_secret=os.getenv('REDDIT'),
    user_agent='AmongUs Meme Scraper',
    username='atquick',
    password=os.getenv('PASS'))

subr = r.subreddit('amongus')

for submission in subr.search("flair:'humor'", limit=50):
    print(submission)
    