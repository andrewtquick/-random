import discord
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context

class CogControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @Command(name='load', hidden=True)
    @commands.has_role('Admin')
    @commands.guild_only()
    async def load_cog(self, ctx: Context, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as err:
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`**: {type(err).__name__} - {err}')
        else:
            await ctx.send(f'{ctx.author.mention} -> **`### SUCCESS ###`** {cog} has been loaded.')

    @Command(name='unload', hidden=True)
    @commands.has_role('Admin')
    @commands.guild_only()
    async def unload_cog(self, ctx: Context, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as err:
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`**: {type(err).__name__} - {err}')
        else:
            await ctx.send(f'{ctx.author.mention} -> **`### SUCCESS ###`** {cog} has been unloaded.')

    @Command(name='reload', hidden=True)
    @commands.has_role('Admin')
    @commands.guild_only()
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
