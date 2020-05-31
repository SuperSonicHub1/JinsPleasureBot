import discord
import praw
import os
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER_AGENT"))

qtgrls = ["!qtgrls", "!qtgirls", "! qtgrls", "! qtgirls"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        activity = discord.Activity(
            name='!qtgirls', type=discord.ActivityType.listening)
        await client.change_presence(activity=activity)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if str(message.channel) != "jins-pleasure-bot":
            return

        if message.content.casefold() in qtgrls:
            for submission in reddit.subreddit("AnimeGirls").new(
                    limit=1):
                await message.channel.send("{0}: {1}".format(
                    submission.title, submission.url))


client = MyClient()
keep_alive()
client.run(os.environ.get("DISCORD_BOT_SECRET"))
