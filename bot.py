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

@bot.command('언로드')
async def unload_extension(ctx, *args):
    success = []
    failed = []
    print('ㅡㅡㅡㅡ 언로드 작업 ㅡㅡㅡㅡ')
    for arg in args:
        try:
            await bot.unload_extension(f'cog.cog_{arg}')
            success.append(arg)
            print(f'{arg} 언로드')
        except:            
            print(f'{arg} 실패')
            failed.append(arg)
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    await ctx.channel.send(f'성공 : {", ".join(success)}\n실패 : {", ".join(failed)}')
        
@bot.command('로드')
async def load_extension(ctx, *args):
    success = []
    failed = []
    print('ㅡㅡㅡㅡ 로드 작업 ㅡㅡㅡㅡ')
    for arg in args:
        try:            
            await bot.load_extension(f'cog.cog_{arg}')
            success.append(arg)
            print(f'{arg} 로드')
        except:
            print(f'{arg} 실패')
            failed.append(arg)    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    await ctx.channel.send(f'성공 : {", ".join(success)}\n실패 : {", ".join(failed)}')

async def load_extensions(bot):
    extensions = [
        'cog.cog_general',
        'cog.cog_member',
        'cog.cog_auth'
    ]

    for extension in extensions:
        print(f'{extension} 실행')
        await bot.load_extension(extension)
