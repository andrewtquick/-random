import discord
import praw
import os
import re
import urllib.request as download
import random
from discord import File
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog


class Memer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @Command(name="meme", help="Serves up a steamy hot Among Us meme, courtesy of Reddit.")
    async def meme(self, ctx: Context):
        
        cwd = os.getcwd()
        meme_path = os.path.join(cwd, './memes')
        meme_channel = ctx.guild.get_channel(759167062831792138)
        chosen_file = random.choice(os.listdir(meme_path))
        chosen_path = os.path.join(meme_path, chosen_file)
        await meme_channel.send(f'{ctx.author.mention}', file=File(chosen_path))
                
def setup(bot):
    bot.add_cog(Memer(bot))