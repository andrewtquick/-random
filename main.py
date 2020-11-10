import discord
import os
from bot_logging.discord_logging import BotLogging
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description="Here are the available commands. \nTo use a command, prefix the command with '!'.")

extensions = [
    'cogs.about',
    'cogs.help',
    'cogs.loadcog',
    'cogs.error_handler',
    'cogs.game',
    'cogs.game_maps',
    'cogs.meme',
    'cogs.misc'
]

@bot.event
async def on_guild_join(guild):
    print(f'New Connection: {guild} -- id: {guild.id}')

@bot.event
async def on_ready():
    print(f'{bot.user} connected.')

    for server in bot.guilds:
        print(f'Connected to: {server} -- id: {server.id}')
    servers = list(bot.guilds)
    print(f'Number of servers: {str(len(servers))}')

if __name__ == '__main__':

    for ext in extensions:
        bot.remove_command('help')
        bot.load_extension(ext)

    TOKEN = os.getenv('TOKEN')
    bot.run(TOKEN)