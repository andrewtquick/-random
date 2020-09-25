import discord
from discord.ext import commands
from discord.ext.commands import Context

class About(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about", help="Information about !Random")
    async def about(self, ctx: Context):
        embed = discord.Embed(title="About", type='rich', colour=discord.Colour(0xf40606), description="!Random was created and developed by Xylr#0781. If you'd like to contribute, please reach out to Xylr on discord directly.\n\nXylr is a novice coder, please be nice. :)")
        embed.set_thumbnail(url="https://i.imgur.com/qwdaLeJ.png")
        embed.add_field(name="Author", value="Xylr#0781", inline=False)
        embed.add_field(name="Github", value="https://github.com/andrewtquick/-random", inline=False)
        embed.add_field(name="Language", value="Python 3.8.3", inline=False)
        embed.add_field(name='Hosting', value="Heroku", inline=False)
        await ctx.author.send(content="Here is information about !Random", embed=embed)


def setup(bot):
    bot.add_cog(About(bot))