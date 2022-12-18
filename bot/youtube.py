import asyncio
import youtube_dl
import discord

from . import config


youtube_dl.utils.bug_reports_message = lambda: ''
ytdl = youtube_dl.YoutubeDL(config.ytdl_format_options)


async def from_url(url, loop=None):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=True))

    if 'entries' in data:
        data = data['entries'][0]

    filename = ytdl.prepare_filename(data)
    return discord.File(filename)
