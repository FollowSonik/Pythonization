from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(result)
