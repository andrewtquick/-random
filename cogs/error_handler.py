import discord
import asyncio
from discord import Forbidden
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown, CommandNotFound, CommandInvokeError

class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, CommandOnCooldown):
            m, s = divmod(float(error.retry_after), 60)
            await ctx.send(f"{ctx.author.mention} - You've previously used that command. You'll need to wait `{int(m)}m {int(s)}s`")
        elif isinstance(error, CommandNotFound):
            pass
        elif isinstance(error, Forbidden):
            pass
        elif isinstance(error, CommandInvokeError):
            user_cmd = ctx.command
            channel = ctx.channel

            error_cause = str(error.original)

            if 'Missing Permissions' in error_cause:
                msg = await ctx.author.send("**I'm missing the `Send Messages` permission.**\n\nTo add this permission, `Go to Server Settings, then go to Roles`. Ensure `@everyone` and my current role have the `Send Messages` permission.\n\nReact to this message with a :white_check_mark: once the permissions have been fixed.")
                await msg.add_reaction('✅')

                try:
                    res = await self.bot.wait_for('reaction_add', timeout=120.0, check=lambda reaction, user: reaction.emoji == '✅')
                    if res:
                        reaction, user = res
                        if reaction.emoji == '✅':
                            await user.send(f'Great! Try the `!{user_cmd}` command again in the `#{channel}` channel.')
                            await user.send('Or, you can send the command here.')
                except asyncio.TimeoutError:
                    await ctx.author.send('Did not see a response from you.')


def setup(bot):
    bot.add_cog(ErrorHandler(bot))