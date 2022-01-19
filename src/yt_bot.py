import discord
from discord import message
from discord.ext import commands
import youtube_dl
import random 
from yahoo_fin import stock_info as si

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
async def welcome(ctx):
    await ctx.send('Welcome to the server')

@client.command()
async def price(ctx, *, stock):
    price = si.get_live_price(stock)
    price_f = "{:,.2f}".format(price)
    await ctx.send(f'The current price of {stock} is ${price_f}')


@client.command()
async def random_number(ctx, min, max):
    await ctx.send(f'Random number between {min} and {max}: {random.randint(min, max)}')

@client.command()
async def flip_a_coin(ctx):
    await ctx.send(f'Coin flip: {random.choice(["Heads", "Tails"])}')
    




@client.command()
async def Help(ctx):
    embed = discord.Embed(title='Help', description='List of commands', color=0xeee657)

    embed.add_field(name='!8ball', value='Ask the magic 8 ball a question', inline=False)
    embed.add_field(name='!clear', value='Clear the chat', inline=False)
    embed.add_field(name='!kick', value='Kick a member', inline=False)
    embed.add_field(name='!ban', value='Ban a member', inline=False)
    embed.add_field(name='!unban', value='Unban a member', inline=False)
    embed.add_field(name='!join', value='Join the voice channel', inline=False)
    embed.add_field(name='!welcome', value='Welcome message', inline=False)
    embed.add_field(name='!price', value='Get the current price of a stock', inline=False)
    embed.add_field(name='!random_number', value='Get a random number', inline=False)
    embed.add_field(name='!flip_a_coin', value='Flip a coin', inline=False)


    await ctx.send(embed=embed)










#OTAxMDE5MjI0NDM5Mzk0MzI1.YXJxiw.8mcrfoq95A2-S8sLRsGWE2FQF_0



client.run('OTMwNDQyMDcxNzQxOTU2MTI2.Yd17tA.7bbGv3jRp7MskZ6ocEgvj__6KeQ')

