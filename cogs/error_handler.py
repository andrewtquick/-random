import discord
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown, CommandNotFound

class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, CommandOnCooldown):
            m, s = divmod(float(error.retry_after), 60)
            await ctx.send(f"{ctx.author.mention} - You've previously requested a random game. You'll need to wait `{int(m)}m {int(s)}s`")
        elif isinstance(error, CommandNotFound):
            await ctx.send(f"{ctx.author.mention} - Sorry, I don't understand that command. try `!help` for a list of commands.")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))