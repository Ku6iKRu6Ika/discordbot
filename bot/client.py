import discord
from . import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def run():
    client.run(config.token)
