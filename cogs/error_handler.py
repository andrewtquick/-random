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
                embed = discord.Embed(title='Missing Permissions', description=f'Missing `Send Messages` and `Manage Messages` permissions on `{ctx.guild}`', colour=discord.Colour(0xe74c3c))
                embed.set_thumbnail(url='https://i.imgur.com/ySoSpp6.png')
                embed.add_field(name='\u200b', value='\u200b', inline=False)
                embed.add_field(name='How to add permission', value='`Go to Server Settings, then go to Roles`.\nEnsure `@everyone` and my other roles have the `Send Messages` and `Manage Messages` permission.', inline=False)
                embed.add_field(name='\u200b', value='\u200b', inline=False)
                embed.add_field(name='Explanation', value='`Send Messages` allows me to post my content to the channel.\n`Manage Messages` allows me to edit my own messages, if I need to. I do not edit others messages.\n```Without these permissions, I will not work properly.```')
                embed.add_field(name='\u200b', value='\u200b', inline=False)
                embed.add_field(name='Completed?', value='React to this message with a :white_check_mark: once the permissions have been fixed.', inline=False)

                msg = await ctx.author.send(embed=embed)
                await msg.add_reaction('✅')

                def check(reaction, user):
                    if user != self.bot.user:
                        return user and reaction

                try:
                    res = await self.bot.wait_for('reaction_add', timeout=120.0, check=check)
                    reaction, _ = res
                    if reaction.emoji == '✅':
                        embed2 = discord.Embed(title='Permission fixed!', colour=discord.Colour(0x2ecc71))
                        embed2.set_thumbnail(url='https://i.imgur.com/ySoSpp6.png')
                        embed2.add_field(name='Try again!', value=f'Try the `!{user_cmd}` command in the `#{channel}` channel in the `{ctx.guild}` server again.')
                        await msg.edit(embed=embed2, delete_after=120)
                                
                except asyncio.TimeoutError:
                    return


def setup(bot):
    bot.add_cog(ErrorHandler(bot))