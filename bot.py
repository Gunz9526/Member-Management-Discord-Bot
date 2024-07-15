import discord
from discord.ext import commands
from util.check_nickname import check_validate_nickname

from app import app
# from start import shared_data


intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))
    print(f'ㅡㅡㅡㅡㅡ {bot.user} 실행 ㅡㅡㅡㅡㅡ')


# 함수 모듈화 예정
@bot.command(name='링크')
async def send_dm(ctx):
    DMchannel = await ctx.author.create_dm()
    nickname = check_validate_nickname(ctx.author.display_name)
    if nickname is not None:
        await DMchannel.send("반갑습니다. " + nickname['clan'] + " 클랜의 " + nickname['role'] + " " + nickname['nickname'] + "님")
    
@bot.command(name='도움')
async def request_help(ctx):
    embed = discord.Embed(title='명령어', description='명령어들의 모음입니다.')
    embed.add_field(name='!링크', value='클랜원 및 블랙리스트 작업이 가능한 링크가 DM으로 전송됩니다.')
    embed.add_field(name='!서버이름', value='현재는 서버이름만 출력. 추후 서버ID기반으로 작업가능')
    embed.add_field(name='!멤버검색', value='해당 문자열이 포함된 디스코드 사용자 검색. 클랜 검색으로 이용할 예정')        
    embed.add_field(name='!멤버추가', value='간단한 클랜원 추가는 이 명령어로 할 수 있도록 시도할 에정')
    await ctx.channel.send(embed=embed, reference=ctx.message)

@bot.command(name='서버이름')
async def request_servername(ctx):
    await ctx.channel.send(ctx.guild.name + ' ' + str(ctx.guild.id), reference=ctx.message)
        
@bot.command(name='클랜원추가')
async def add_clan_member(ctx, *args):
    with app.app_context():
        from controller.controller_member import MemberController
        member_object = MemberController()
        clan_name = check_validate_nickname(ctx.author.display_name)

        clan_id = member_object.retrieve_clan_id(clan_name['clan_name'])
        for i in range(len(args)):
            member_object.add_clan_member(clan_id=clan_id, nickname=args[i])

    await ctx.channel.send(clan_name['clan_name'] + '클랜에 ' + ', '.join(args) + '이 추가되었습니다.', reference=ctx.message)

@bot.command('클랜원검색')
async def retrieve_member(ctx, args):
    with app.app_context():
        from controller.controller_member import MemberController
        member_object = MemberController()
        clan_name = check_validate_nickname(ctx.author.display_name)
        clan_id = member_object.retrieve_clan_id(clan_name['clan_name'])
        member_list = member_object.retrieve_clan_member(nickname=args, clan_id=clan_id)
        
        print(type(member_list))
        embed = discord.Embed(title='클랜원 목록', description=f'{clan_name["clan_name"]}클랜의 검색된 클랜 멤버 입니다.')        
        embed.add_field(name=f'멤버 ( {len(member_list)}명 )', value='\n'.join(member_list), inline=False)
        await ctx.channel.send(embed=embed, reference=ctx.message)

@bot.command('블랙리스트검색')
async def retrieve_blacklist(ctx, args):
    with app.app_context():
        from controller.controller_member import MemberController
        member_object = MemberController()
        member_list = member_object.retrieve_blacklist(nickname=args)
        print(type(member_list))
        embed = discord.Embed(title='블랙리스트')
        embed.add_field(name=f'멤버 ( {len(member_list)}명 )', value='\n'.join(member_list), inline=False)
        await ctx.channel.send(embed=embed, reference=ctx.message)


@bot.command(name='나는고수냐')
async def gosu(ctx):
    nickname = check_validate_nickname(ctx.author.display_name)
    await ctx.channel.send(f"말씀중에 죄송합니다. {nickname['nickname']} 저얼대 월드클래스 아닙니다.")
