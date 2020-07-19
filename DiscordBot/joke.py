from options import client
import joke_api


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pog'):
        joke = joke_api.get_joke()
        print(joke)

        if joke == False:
            await message.channel.send('feelsbad..')
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])
