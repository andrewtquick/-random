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
        embed = discord.Embed(title='The Skeld Map', colour=discord.Colour(0x1f8b4c))
        embed.set_image(url=skeld)
        embed.add_field(name='Below is the map of Skeld', value="Click for a larger version")
        embed.set_footer(text='Image courtesy of Innersloth, developers of Among Us')
        await ctx.send(embed=embed)
    
    @Command(name='mira', help='Display a map of MiraHQ')
    @commands.has_permissions(send_messages=True)
    async def mira(self, ctx: Context):
        mira = 'https://i.imgur.com/wdGIyMJ.png'
        embed = discord.Embed(title='MiraHQ Map', colour=discord.Colour(0xe74c3c))
        embed.set_image(url=mira)
        embed.add_field(name='Below is the map of MiraHQ', value="Click for a larger version")
        embed.set_footer(text='Image courtesy of Innersloth, developers of Among Us')
        await ctx.send(embed=embed)

    @Command(name='polus', help='Display a map of Polus')
    @commands.has_permissions(send_messages=True)
    async def polus(self, ctx: Context):
        polus = 'https://i.imgur.com/2E2lEpx.png'
        embed = discord.Embed(title='POLUS Map', colour=discord.Colour(0x71368a))
        embed.set_image(url=polus)
        embed.add_field(name='Below is the map of POLUS', value="Click for a larger version")
        embed.set_footer(text='Image courtesy of Innersloth, developers of Among Us')
        await ctx.send(embed=embed)

    @Command(name='airship', help='Display a map of Airship')
    @commands.has_permissions(send_messages=True)
    async def airship(self, ctx: Context):
        airship = 'https://i.imgur.com/4cdwXi5.png'
        embed = discord.Embed(title='Airship Map', colour=discord.Colour(0x71368a))
        embed.set_image(url=airship)
        embed.add_field(name='Below is the map of Airship', value="Click for a larger version")
        embed.set_footer(text='Image courtesy of Innersloth, developers of Among Us')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GameMaps(bot))