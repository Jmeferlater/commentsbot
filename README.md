# commentsbot
A Reddit bot which reads through a given user's comments, looking for a given word, and replies with the percentage of times that person used the given word

Looks through the comments on /r/all, listening for the command !Comments, followed by a user and a word to look for

The bot will then go to the given user's comment history and count every comment that uses the given word and will reply with the percentage of comments that uses said word.

an example of a call to the bot is:

"!Comments USER WORD"

an example of the bot's reply is:

"25% of this person's comments included the word WORD"
