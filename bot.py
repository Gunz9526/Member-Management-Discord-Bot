import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))
    print(f'봇 {client.user} 대기중')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!테스트'):
        await message.channel.send('Consider it done.')

    if message.content.startswith('!링크'):
        DMchannel = await client.create_dm(message.author)
        nickname = message.author.display_name.split('/')
        await DMchannel.send("반갑습니다. " + nickname[0] + " 클랜의 " + nickname[2] + " " + nickname[1] + "님")
