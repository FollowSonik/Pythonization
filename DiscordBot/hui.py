from options import client


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$hui':
        await message.channel.send('pizda')
