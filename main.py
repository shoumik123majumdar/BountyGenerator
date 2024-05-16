import os
import praw
from fuzzywuzzy import fuzz
import pandas as pd
import csv
from text_validator import Text_Validator

'''
PLAN:
- Get all of the data/comments, from each post (only posts labeled analysis)
- Combine the upvotes, downvotes, and Sentiment Analysis score into a single popularity score for each character.
- 
- Clean text: (WATCH VIDEO)
- Sentiment analyzer class
    - Inputs: Cleaned_text, characters within text. 
    - Outputs: Dictionary of character --> sentiment score + num_upvotes
- Final Bounty calculator (function or class TBD)
    - Inputs: For each character... --> Make this into a a database using SQL or something of the sort. 
        - voting 
        - average sentiment score among all comments regarding them
    - Outputs: Bounty Value
'''


CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")
USER_NAME = os.environ.get("USER_NAME")


reddit = praw.Reddit(
    client_id= CLIENT_ID,
    client_secret=SECRET_ID,
    user_agent= USER_NAME
)


subreddit = reddit.subreddit('OnePiecePowerScaling')
time_range = 'week'  # can also use day, month, year

#Creates a list of the top posts (number of posts = limit) from our time_range (in this case a week)
post_list = subreddit.top(time_filter = time_range)


inclusion_phrases = ['Who wins', "Tier List", "strongest", "weaker", "stronger", "weakest"]
character_list = []
with open('characters.csv',newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        character_list.extend([value for value in row if value])


text_validator = Text_Validator(character_list)


data_posts = []
for post in post_list:
    if text_validator.is_valid_text(post.title):
        post_data = {
            "title" : post.title.lower(), #small things to clean the data while processing it to make it easier in the future
            "num_votes" : post.score,
            "comments" : []
        }

        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if text_validator.is_valid_text(comment.body):
                comment_tuple = tuple([comment.body.lower(),comment.score])
                post_data["comments"].append(comment_tuple)

        data_posts.append(post_data)
print(data_posts)


#Structure the text_validation into a specialized class. This way it can be reused in other classes.