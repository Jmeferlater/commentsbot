

import praw
import os
import time
from config_bot import *

if not os.path.isfile("config_bot.py"):
    print("You must create a config file with your username and password.")
    exit(1)

user_agent = ("replies back with percentage of comments using given string in given user's history 0.1")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASS)
subreddit = r.get_subreddit('all')
keyword = "!comments"
alreadyDone = set()

def comment():
    print("searching")
    lis =[]
    try:
        all_comments = subreddit.get_comments(limit=100)
        for comment in all_comments:
            commentbody = comment.body.lower()
            if (keyword in commentbody) and (comment.id not in alreadyDone):
                alreadyDone.add(comment.id)
                arguments = commentbody.split("!comments", 1)
                print(arguments)
                commands = arguments[1].split()
                print(commands)
                redditor = r.get_redditor(commands[0])
                comments = redditor.get_comments()
                inputstring = " " + commands[1] + " "
                print(inputstring)
                comment.reply(reply_to_comment(comments, inputstring))
    except Exception as error:
        print("Error recieved")
        print(error)

def reply_to_comment(comments, inputstring):
    total = 0
    contains = 0
    for comment in comments:
        total += 1
        if inputstring in comment.body:
            contains += 1
    print(str(total))
    print(str(contains))
    return str(round((contains/total) * 100)) + "%" + " of this person's comments included the word" + inputstring

print("searching for keywords")

while True:
    comment()
    print("Sleeping...")
    time.sleep(30)
    print("Starting...")


