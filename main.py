import discord
import os
from bot_logging.discord_logging import BotLogging
from discord.ext import commands

from boto.s3.connection import S3Connection

bot = commands.Bot(command_prefix='!')

extensions = [
    'cogs.game',
    'cogs.loadcog',
    'cogs.error_handler',
]

@bot.event
async def on_ready():
    print(f'{bot.user} connected.')
    BotLogging.LOGGER.info(f'Connected to server:')
    for server in bot.guilds:
        BotLogging.LOGGER.info(server)

if __name__ == '__main__':

    for ext in extensions:
        bot.load_extension(ext)

    # TOKEN = open('token.txt', 'r').read()
    TOKEN = S3Connection(os.environ['TOKEN'])
    bot.run(os.environ.get('TOKEN'))