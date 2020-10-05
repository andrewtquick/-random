import discord
from discord.ext import commands
from discord.ext.commands import Context

class CogControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @commands.has_role('Admin')
    async def load_cog(self, ctx: Context, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as err:
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`**: {type(err).__name__} - {err}')
        else:
            await ctx.send(f'{ctx.author.mention} -> **`### SUCCESS ###`** {cog} has been loaded.')

    @commands.command(name='unload', hidden=True)
    @commands.has_role('Admin')
    async def unload_cog(self, ctx: Context, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as err:
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`**: {type(err).__name__} - {err}')
        else:
            await ctx.send(f'{ctx.author.mention} -> **`### SUCCESS ###`** {cog} has been unloaded.')

    @commands.command(name='reload', hidden=True)
    @commands.has_role('Admin')
    async def reload_cog(self, ctx: Context, *, cog: str):

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as err:
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`**: {type(err).__name__} - {err}')
        else:
            await ctx.send(f'{ctx.author.mention} -> **`### SUCCESS ###`** {cog} has been reloaded.')

def setup(bot):
    bot.add_cog(CogControl(bot))
