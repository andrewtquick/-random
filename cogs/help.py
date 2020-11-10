import discord
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', help='The help command')
    async def help(self, ctx: Context, cog='all'):

        embed = discord.Embed(title='Help', color=discord.Colour(0xF1C40F), description='List of available bot commands for !Random.')
        embed.set_thumbnail(url='https://i.imgur.com/ySoSpp6.png')
        embed.add_field(name='Commands', value='Ensure you prefix the command with a "!"', inline=False)

        cogs = [cog for cog in self.bot.cogs.keys()]
        cogs.sort()
        cogs.remove('CogControl')
        cogs.remove('ErrorHandler')

        if cog == 'all':
            for cog in cogs:
                cog_command = self.bot.get_cog(cog).get_commands()

                for command in cog_command:
                    embed.add_field(name=command.name, value=command.help, inline=False)

        else:

            lower_cogs = [cog.lower() for c in cogs]

            if cog.lower() in lower_cogs:
                commands = self.bot.get_cog(cogs[lower_cogs.index(cog.lower())]).get_commands()
                help_text = ''

                for command in commands:
                    help_text += f'```{command.name}```\n**{command.help}**\n\n'
                    help_text += f'Format: !{command.name} {command.usage if command.usage is not None else ""}\n'
                embed.description = help_text
            
        await ctx.send(f'{ctx.author.mention}', embed=embed)
            

            


def setup(bot):
    bot.add_cog(Help(bot))