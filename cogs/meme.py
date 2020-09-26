import discord
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog

class Memer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def meme(self, ctx: Context):
        pass

def setup(bot):
    bot.add_cog(Memer(bot))