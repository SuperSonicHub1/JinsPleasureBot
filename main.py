import discord
import praw
import os
from keep_alive import keep_alive

# Get access to the Reddit API.
reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER_AGENT"))

# Allow for the use of multiple commands; the last two have spaces to fight against mobile autocorrect.
qtgrls = ["!qtgrls", "!qtgirls", "! qtgrls", "! qtgirls"]

# Actual code starts here.
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        # Custom status.
        activity = discord.Activity(
            name='!qtgirls', type=discord.ActivityType.listening)
        await client.change_presence(activity=activity)

    async def on_message(self, message):
        # Don't respond to ourselves.
        if message.author == self.user:
            return

        # Stops bot from being spammed throughout the server.
        if str(message.channel) != "jins-pleasure-bot":
            return
        
        # Sends the message.
        if message.content.casefold() in qtgrls:
            for submission in reddit.subreddit("AnimeGirls").new(
                    limit=1):
                await message.channel.send("{0}: {1}".format(
                    submission.title, submission.url))


client = MyClient()
keep_alive()
client.run(os.environ.get("DISCORD_BOT_SECRET"))
