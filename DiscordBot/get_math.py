from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from pathlib import Path
import math_api

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN')


# command = '$math'

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print('Pig! From the Math API!')


@client.command()
async def math(ctx, *string):
    if string.__contains__('+'):
        pigchemp = '{}'.format('%2B'.join(string))
        result = math_api.get_math(pigchemp)
        await ctx.send(result)
    else:
        pigchemp = '{}'.format(''.join(string))
        result = math_api.get_math(pigchemp)
        await ctx.send(result)

    # await ctx.send(result)

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
