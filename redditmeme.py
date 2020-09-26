import praw
import os
import re
import urllib.request as download

r = praw.Reddit(
    client_id='9sMbfS0kHaVZlQ',
    client_secret=os.getenv('REDDIT'),
    user_agent='AmongUs Meme Scraper',)

subr = r.subreddit('amongus')

main_path = os.getcwd()
meme_path = os.path.join(main_path, 'memes')

if not os.path.isdir('memes'):
    os.mkdir(meme_path)

for submission in subr.search("flair:'humor'", limit=200):
    if submission.url.endswith('jpg'):
        jpg_filename = re.search(r'\w+.jpg',submission.url).group(0)
        if not os.path.isfile(f'./memes/{jpg_filename}'):
            download.urlretrieve(submission.url, f'./memes/{jpg_filename}')
    elif submission.url.endswith('png'):
        png_filename = re.search(r'\w+.png', submission.url).group(0)
        if not os.path.isfile(f'./memes/{png_filename}'):
            download.urlretrieve(submission.url, f'./memes/{png_filename}')