import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ㅎㅇ'))
    print(f'봇 {client.user} 대기중')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!테스트'):
        await message.channel.send('Consider it done.')

    if message.content.startswith('!ㅎㅇ'):
        DMchannel = client.create_dm(message.author)
        await DMchannel.send("State your will.")
