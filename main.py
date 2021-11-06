import discord
import requests
import json

token = "OTA1OTMyODAxNjc1NzY3ODU4.YYRRqw.xESG-dh1ng2DFTXJuGIV-F4JQAc"
client = discord.Client()

#to get quotes
def get_dundies():
    response = requests.get('https://officeapi.dev/api/quotes/random')
    json_data = json.loads(response.text)
    quote = json_data['data'] ['content'] + "  -" + json_data['data'] ['character'] ['firstname']
    return quote


#to start bot
@client.event
async def on_ready():
    print( 'I am {0.user} '.format(client))

#to send messages and replies
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$michael'):
        quote = get_dundies()
        await message.channel.send(quote)

client.run(token)
