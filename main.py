import os
import praw
from fuzzywuzzy import fuzz
import pandas as pd

'''
PLAN:
- Get all of the data/comments, from each post (only posts labeled analysis)
- 
'''

# When using an API, you don't want to give out sensitive information in your code directly.
# Utilizing environment variables allows you to securely access this information
# without publishing it directly in your code.
CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")
USER_NAME = os.environ.get("USER_NAME")

# Creates an instance of the reddit object from PRAW.
# This is the object we will manipulate in order to extract the data we want
reddit = praw.Reddit(
    client_id= CLIENT_ID,
    client_secret=SECRET_ID,
    user_agent= USER_NAME
)

subreddit = reddit.subreddit('OnePiecePowerScaling')  # stores the subreddit we will be working with
time_range = 'week'  # can also use day, month, year

#Creates a list of the top posts (number of posts = limit) from our time_range (in this case a week)
post_list = subreddit.top(time_filter = time_range,limit=25)
print(type(post_list))

filtered_posts = []
for post in post_list:
    if post.link_flair_text != "Poll":






