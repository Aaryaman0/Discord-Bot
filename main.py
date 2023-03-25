import discord
import openai
import ai

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    D = {"Cucumberbatch" : "Aaryaman", "hb" : "Hans", "bearpooh" : "Winston", "SoaringMonkey13" : "Maanav", "Aaditya" : "Aaditya"}
    if message.author == client.user:
        return

    #if str(message.author) == "Cucumberbatch#2932":
    #    await message.channel.send("hi")
    
    if str(message.author) == "SoaringMonkey13#2781":
        final = ai.insult("Maanav")
        await message.channel.send(final)
    
    m = message.content

    if (message.mentions != []) :
        if (message.mentions[0].display_name == "WinstonBot") :
            await message.channel.send("a")
            username = ""
            # await message.channel.send(message.content)
            if ("insult" in str(message.content)):
                username = message.mentions[1].name
                await message.channel.send("b")
                name = D[username]
                if ("about" in str(message.content)):
                    start = str(message.content).find("about") + 3
                    final = ai.insult(name, str(message.content)[start:])
                    await message.channel.send(final)
                else:
                    final = ai.insult(name, "")
                    await message.channel.send(final)
        # await message.channel.send(message.mentions)
    
    if message.content.startswith('@WinstonBot  insult Aaryaman'):
        await message.channel.send(message.content)

    if message.content.startswith('🍇'):
        await message.channel.send('🍇')

    #if (message.mentions[0].display_name == "WinstonBot") :
    #    names = []
    #    await message.channel.send(names)
    #    if ("insult" in message.content):
    #        for name in message.mentions : names.append(name.id)
    #    await message.channel.send(names)
    
    #if str(message.author) == "hb#3238":
    #    await message.channel.send('Boke')
    
    #if str(message.author) == "SoaringMonkey13#2781":
    #    await message.channel.send('But why?')

    #if str(message.author) == "Bearpooh#0625":
    #    await message.channel.send('50 can')

    #if str(message.author) == "Lenopix#9999":
    #    await message.channel.send(':smiley_cat:')
    
    #if str(message.author) == "Cucumberbatch#2932":
    #    await message.channel.send(':clown: Simp')
    
    #if str(message.author) == "Aaditya#3260":
    #    await message.channel.send('PUUHFECT')

client.run()