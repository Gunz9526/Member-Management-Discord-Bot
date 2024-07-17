import discord
from discord.ext import commands


intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await load_extensions(bot)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))
    print(f'ㅡㅡㅡㅡㅡ {bot.user} 실행 ㅡㅡㅡㅡㅡ')


async def load_extensions(bot):
    extensions = [
        'cog.cog_general',
        'cog.cog_member'
    ]

    for extension in extensions:
        print(f'{extension} 실행')
        await bot.load_extension(extension)
