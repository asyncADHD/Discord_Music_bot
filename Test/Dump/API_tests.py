# import requests 
# import googleapiclient.discovery


# api_service_name = "youtube"
# api_version = 'v3'

# DEVELOPER_KEY = ""

# # API_CLIENT 

# youtube = googleapiclient.discovery.build(
#     api_service_name, api_version, developerKey=DEVELOPER_KEY)

# # request variable is the only thing needed to be changed 


# request = youtube.search().list(
#     part="id,snippet",
#     type="video",
#     q="summer of 69",
#     videoDuration="any",
#     maxResults="1"
# )

# response = request.execute()

# print (response)


''' 
- take the vedio url out of the api request 
- take the vedio url and put it into a variable
- put it into the vlc and pafy lib 

'''


from discord import channel
from youtubesearchpython import *

def Discord_MV_url():
    variable = input("Enter a search term: ")
    customsearch = CustomSearch(variable, VideoSortOrder.viewCount,limit=1)

    for i in range(1):
        return (customsearch.result()['result'][i]['link'])

print (Discord_MV_url()) 




import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'OTAxMDE5MjI0NDM5Mzk0MzI1.YXJxiw.8mcrfoq95A2-S8sLRsGWE2FQF_0'
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()



