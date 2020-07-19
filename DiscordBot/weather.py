from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from pathlib import Path
import weather_api

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN')

# command = '$weather'

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print('Pig! From the weather!')


@client.command()
async def weather(ctx, city):
    weather = weather_api.get_weather(city)
    await ctx.send(weather)

    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return

    #     if message.content.startswith(command):
    #         print(pog)
    #         weather = weather_api.get_weather()
    #         print(weather)

    #     if weather == False:
    #         await message.channel.send('feelsbad..')
    # else:
    # await message.channel.send(weather)

client.run(TOKEN)
