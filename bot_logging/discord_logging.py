import discord
import logging

class BotLogging():
    
    LOGGER = logging.getLogger('discord')
    LOGGER.setLevel(logging.DEBUG)
    HANDLER = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    HANDLER.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    LOGGER.addHandler(HANDLER)