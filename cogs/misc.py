import discord
import pytz
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog

class CurrentTime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @Command(name='time', help='Get current date and time from around the globe.')
    async def time(self, ctx: Context):

        tz = {
            'Etc/GMT': '',
            'WET': '',
            'CET': '',
            'EET': '',
            'Etc/GMT+3': '',
            'US/Alaska': '',
            'US/Eastern': '',
            'US/Central': '',
            'US/Mountain': '',
            'US/Pacific': '',
            'US/Hawaii': '',
            'Canada/Atlantic': ''
        }

        for i in tz:
            zone = pytz.timezone(i)
            time = datetime.now(zone)
            tz[i] = time.strftime('%Y/%m/%d :: %I:%M %p')

        embed = discord.Embed(title='Current Time around the world', colour=(0x11806a))
        embed.add_field(name='GMT' , value=tz['Etc/GMT'])
        embed.add_field(name='WEST' , value=tz['WET'])
        embed.add_field(name='CEST' , value=tz['CET'])
        embed.add_field(name='EEST' , value=tz['EET'])
        embed.add_field(name='MSK' , value=tz['Etc/GMT+3'])
        embed.add_field(name='AST' , value=tz['US/Alaska'])
        embed.add_field(name='EST' , value=tz['US/Eastern'])
        embed.add_field(name='CST' , value=tz['US/Central'])
        embed.add_field(name='MST' , value=tz['US/Mountain'])
        embed.add_field(name='PST' , value=tz['US/Pacific'])
        embed.add_field(name='HST' , value=tz['US/Hawaii'])
        embed.add_field(name='AKST' , value=tz['Canada/Atlantic'])

        await ctx.send(f'{ctx.author.mention}', embed=embed)

def setup(bot):
    bot.add_cog(CurrentTime(bot))