from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('PogChamp!')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1e3, 3)}ms')


client.run(TOKEN)
