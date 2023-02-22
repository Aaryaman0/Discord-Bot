import discord
import openai

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(':grapes:'):
        await message.channel.send(':grapes:')
    
    if str(message.author) == "hb#3238":
        await message.channel.send('Boke')
    
    if str(message.author) == "SoaringMonkey13#2781":
        await message.channel.send('But why?')

    if str(message.author) == "Bearpooh#0625":
        await message.channel.send('50 can')

    if str(message.author) == "Lenopix#9999":
        await message.channel.send(':smiley_cat:')
    
    if str(message.author) == "Cucumberbatch#2932":
        await message.channel.send(':clown: Simp')
    
    if str(message.author) == "Aaditya#3260":
        await message.channel.send('PUUHFECT')

client.run('')