import discord
import random
import time
import asyncio


TOKEN = "ODYwNjAwMTU2Njg3NDMzNzI4.YN9mWg.bTTUQZ60UMzC0vn1IhwXNdVeVxo"

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".pnw"):
        await message.channel.send("CR0Gs previous networth was $246,752,898")

@client.event
async def on_ready():
    print("running pog")

client.run(TOKEN)