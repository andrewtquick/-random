import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @Command(name='help', help='The help command')
    @commands.guild_only()
    async def help(self, ctx: Context, cog='all'):
        
        embed = discord.Embed(title='Help', color=discord.Colour(0xF1C40F), description="Here you'll find a book of different commands that I know.")
        embed.set_thumbnail(url='https://i.imgur.com/ySoSpp6.png')
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name='Commands', value='Ensure you prefix the command with a "!"', inline=False)
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name='Navigating the Help Book',
                        value=f'''Use the \u23ea and \u25c0 to go back to previous pages.\n
                        Use \u25b6 and \u23e9 to advance the pages.\n
                        Using \u274c will delete the help display. It will delete itself if left idle''',
                        inline=False)
                
        embed_pages = [embed]

        cogs = [cog for cog in self.bot.cogs.keys()]
        cogs.remove('CogControl')
        cogs.remove('ErrorHandler')

        if cog == 'all':
            for cog in cogs:
                cog_command = self.bot.get_cog(cog).get_commands()
                for command in cog_command:
                    embed_pages.append(
                        discord.Embed(title=command.name.capitalize(), description=command.help, colour=discord.Colour(0xF1C40F))
                        .set_thumbnail(url='https://i.imgur.com/ySoSpp6.png')
                        .add_field(name='\u200b', value='\u200b', inline=False)
                        .add_field(name='Usage:', value=f'```!{command.name} {command.usage if command.usage is not None else ""}```'))

        msg = await ctx.send(embed=embed_pages[0], delete_after=120.0)
        emojis = ['\u23ea', '\u25c0', '\u25b6', '\u23e9', '\u274c']

        for e in emojis:
            await msg.add_reaction(e)

        def check(reaction, user):
            if user != self.bot.user:
                return user and reaction

        selected_page = 0
        selected_emoji = ''
        
        while True:
            if selected_emoji == '\u23ea':
                selected_page = 0
                embed_msg = embed_pages[selected_page].set_footer(text='\u0020')
                await msg.edit(embed=embed_msg)
                
            if selected_emoji == '\u25c0':
                if selected_page >= 1:
                    selected_page -= 1
                    if selected_page == 0:
                        embed_msg = embed_pages[selected_page].set_footer(text='\u0020')
                    else:
                        embed_msg = embed_pages[selected_page].set_footer(text=f'Page {selected_page} of {int(len(embed_pages))-1}')
                    await msg.edit(embed=embed_msg)
            
            if selected_emoji == '\u25b6':
                if selected_page < len(embed_pages):
                    selected_page += 1
                    embed_msg = embed_pages[selected_page].set_footer(text=f'Page {selected_page} of {int(len(embed_pages))-1}')
                    await msg.edit(embed=embed_msg)
            
            if selected_emoji == '\u23e9':
                selected_page = int(len(embed_pages))-1
                embed_msg = embed_pages[selected_page].set_footer(text=f'Page {selected_page} of {int(len(embed_pages))-1}')
                await msg.edit(embed=embed_msg)
            
            if selected_emoji == '\u274c':
                await msg.edit(suppress=True, delete_after=0.1)

            res = await self.bot.wait_for('reaction_add', timeout=120.0, check=check)
            
            if res == None:
                await self.bot.delete_message(msg)
                for e in emojis:
                    await msg.remove_reaction(e, self.bot.user)
                break
            selected_emoji = res[0].emoji
            await msg.remove_reaction(res[0].emoji, res[1])

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))