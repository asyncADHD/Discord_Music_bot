import discord
import os
from youtubesearchpython import *
from discord.ext import commands


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!',intents=intents)


client = discord.Client()

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

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

    if message.content.startswith('$P'):
        unstripedvar = message.content
        stripedvar = unstripedvar.strip('$P')
        print(stripedvar)
        
        variable = stripedvar
        customsearch = CustomSearch(variable, VideoSortOrder.viewCount,limit=1)

        for i in range(1):
            URL = (customsearch.result()['result'][i]['link'])
        
        await message.channel.send((URL))

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()








client.run('OTAxMDE5MjI0NDM5Mzk0MzI1.YXJxiw.8mcrfoq95A2-S8sLRsGWE2FQF_0')
