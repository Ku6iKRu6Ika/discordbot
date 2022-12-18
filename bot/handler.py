from .client import client
from . import youtube

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(ctx):
    if ctx.author != client.user:
        print(f'Message from {ctx.author}: {ctx.content}')

        await ctx.reply('Загрузка...')
        file = await youtube.from_url(ctx.content, loop=client.loop)
        await ctx.reply(file=file)
