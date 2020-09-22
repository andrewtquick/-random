import discord
from discord.ext import commands
from discord.ext.commands import Context

class About(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about", help="Information about !Random")
    async def about(self, ctx: Context):
        pass

def setup(bot):
    bot.add_cog(About(bot))