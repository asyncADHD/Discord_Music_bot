import discord
from discord import message
from discord.ext import commands
import youtube_dl
import random 

client = commands.Bot(command_prefix='!')
players = {}

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game("I'm jamming"))



@client.event 
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

def is_me(ctx):
    return ctx.author.id == 425577187387768842

# @client.command()
# @commands.check()
# async def Is_it_me(is_me):
#     await is_me.send(f'Hi {is_me.author.mention}')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def play(ctx, url):
    server = ctx.message.guild
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()










#OTAxMDE5MjI0NDM5Mzk0MzI1.YXJxiw.8mcrfoq95A2-S8sLRsGWE2FQF_0



client.run('OTMwNDQyMDcxNzQxOTU2MTI2.Yd17tA.vJWOjhfn2LM5HOgpzZy4hA85GI8')

