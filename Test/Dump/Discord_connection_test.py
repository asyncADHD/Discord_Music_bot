import discord
import os

# i really dont know why this is not working

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Yo, what\'s up?')

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    if message.content.startswith('$test'):
        await message.channel.send('Test!')
    
    if message.content.startswith('$date'):
        var = os.popen('date').read()
        
        await message.channel.send(var)

    if message.content.startswith('$help'):
        await message.channel.send('Hi, I\'m a bot!, If I don\'t respond to you, please contact the owner of this bot.')


        

client.run('OTAxMDE5MjI0NDM5Mzk0MzI1.YXJxiw.8mcrfoq95A2-S8sLRsGWE2FQF_0')