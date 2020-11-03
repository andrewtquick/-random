import discord
import praw
import os
import random
import asyncio
from discord import File
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog


class Memer(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Command(name="meme", help="Serves up a steamy hot Among Us meme, courtesy of Reddit.")
    @commands.has_permissions(send_messages=True)
    async def meme(self, ctx: Context):
        
        memes = []

        async with ctx.channel.typing():
            if len(memes) == 0:
                r = praw.Reddit(
                    client_id='9sMbfS0kHaVZlQ',
                    client_secret=os.getenv('REDDIT'),
                    user_agent='AmongUs Meme Scraper',
                    username=os.getenv('USER'),
                    password=os.getenv('PASS'))

                subr = r.subreddit('amongus')

                for submission in subr.search("flair:'humor'", limit=50):
                    if submission.url.endswith('jpg'):
                        memes.append(submission.url)
                    elif submission.url.endswith('png'):
                        memes.append(submission.url)

            chosen_meme = random.choice(memes)
            memes.remove(chosen_meme)
            await asyncio.sleep(1)
            await ctx.send(f'{ctx.author.mention} - {chosen_meme}')

                
def setup(bot):
    bot.add_cog(Memer(bot))