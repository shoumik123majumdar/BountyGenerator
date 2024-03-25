import os
import praw
from fuzzywuzzy import fuzz
import pandas as pd
import csv

'''
PLAN:
- Get all of the data/comments, from each post (only posts labeled analysis)
- Combine the upvotes, downvotes, and Sentiment Analysis score into a single popularity score for each character.
- 
- Clean text: (WATCH VIDEO)
- Sentiment analyzer class
    - Inputs: Cleaned_text, characters within text. 
    - Outputs: Dictionary of character --> sentiment score
- Final Bounty calculator (function or class TBD)
    - Inputs: For each character...
        - total upvotes
        - total downvotes
        - average sentiment score among all comments regarding them
    - Outputs: Bounty Value
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


inclusion_phrases = ['Who wins', "Tier List"]
character_list = []
with open('characters.csv',newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        character_list.extend([value for value in row if value])



def is_valid_post(post_title):
    for word in post_title.split():
        if word in character_list or word in inclusion_phrases:
            return True
    return False

filtered_posts = []
for post in post_list:
    if is_valid_post(post.title):
        print(post.title)

