import discord
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', help='The help command')
    @commands.has_permissions(send_messages=True)
    async def help(self, ctx: Context, cog='all'):

        embed = discord.Embed(title='Help', color=discord.Colour(0xF1C40F), description='List of available commands for !Random.')
        embed.set_thumbnail(url='https://i.imgur.com/ySoSpp6.png')
        embed.add_field(name='Commands', value='Ensure you prefix the command with a "!"', inline=False)
        embed.add_field(name='\u200b', value='\u200b', inline=False)

        cogs = [cog for cog in self.bot.cogs.keys()]
        cogs.remove('CogControl')
        cogs.remove('ErrorHandler')

        if cog == 'all':
            for cog in cogs:
                cog_command = self.bot.get_cog(cog).get_commands()
                commands = ''

                for command in cog_command:
                    commands += f'**{command.name}** - *{command.help}*\n'
                    embed.add_field(name=command.name, value=command.help, inline=False)

        else:

            cog_command = self.bot.get_command(cog)
            help_text = f'```{cog_command.name}```\n' \
                f'**{cog_command.help}**'

            embed.description = help_text
            embed.remove_field(0)
            embed.remove_field(1)
            embed.add_field(name=f'Format:', value=f'`!{cog_command.name} {cog_command.usage if cog_command.usage is not None else ""}`')

        await ctx.send(f'{ctx.author.mention}', embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))