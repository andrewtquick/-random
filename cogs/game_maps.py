import discord
import requests
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog

class GameMaps(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Command(name='skeld', help='Display a map of The Skeld')
    @commands.has_permissions(send_messages=True)
    async def skeld(self, ctx: Context):
        skeld = 'https://i.imgur.com/lQUSrhv.png'
        await ctx.send(skeld)
    
    @Command(name='mira', help='Display a map of MiraHQ')
    @commands.has_permissions(send_messages=True)
    async def mira(self, ctx: Context):
        mira = 'https://i.imgur.com/wdGIyMJ.png'
        await ctx.send(mira)

    @Command(name='polus', help='Display a map of Polus')
    @commands.has_permissions(send_messages=True)
    async def polus(self, ctx: Context):
        polus = 'https://i.imgur.com/2E2lEpx.png'
        await ctx.send(polus)


def setup(bot):
    bot.add_cog(GameMaps(bot))