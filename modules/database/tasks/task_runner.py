import asyncio

import discord

from modules.cryptocurrency.crypto import get_info
from .db import get_tasks

messages = {}


async def run_tasks(client):
    await client.wait_until_ready()
    channel = discord.Object(id='422504096990494741')
    while not client.is_closed:
        tasks = get_tasks()
        for service, request in tasks:
            text = get_info(request)
            if request in messages:
                message = messages[request]
                await client.edit_message(message, text)
                return
            message = await client.send_message(channel, text)
            messages[request] = message
        await asyncio.sleep(120)
