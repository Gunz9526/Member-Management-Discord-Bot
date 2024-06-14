import discord
from discord.ext import commands


intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))
    print(f'ㅡㅡㅡㅡㅡ {client.user} 실행 ㅡㅡㅡㅡㅡ')


# 함수 분리 예정
@client.event
async def on_message(message):
    # 봇이 보낸 메세지는 읽어들이면 안됨.
    if message.author == client.user:
        return

    # 멤버 CRUD 작업을 위한 개인용 링크를 DM으로 전송. 
    if message.content.startswith('!링크'):
        DMchannel = await client.create_dm(message.author)
        nickname = message.author.display_name.split('/')
        if len(nickname) > 2:
            await DMchannel.send("반갑습니다. " + nickname[0] + " 클랜의 " + nickname[2] + " " + nickname[1] + "님")
        else:
            await DMchannel.send("반갑습니다. " + message.author.display_name + "님 닉네임을 형식에 맞게 변경해주세요")

    # flask app 과 데이터 공유 에정, 아직 방법 구상 중
    if message.content.startswith('!멤버추가'):
        input_string = message.content.split(" ", maxsplit=1)
        if len(input_string) > 1:
            add_user = check_validate_nickname(input_string)
            await message.channel.send('멤버 ' + add_user[0])
        else:
            await message.channel.send('추가 할 멤버를 정확히 입력해주세요')

    # 도움말, 명령어 나열 예정
    if message.content.startswith('!도움'):
        await message.channel.send('Consider it done.')

    # 길드 ID 및 이름 return 가능
    if message.content.startswith('!서버이름'):
        await message.channel.send(message.channel.guild.name + ' ' + str(message.channel.guild.id))
    
    # 클랜 검색, 클랜원 검색 예정
    if message.content.startswith("!멤버검색"):
        input_string = message.content.split(" ", maxsplit=1)
        if len(input_string) > 1:
            result = await message.channel.guild.query_members(input_string[1])
            if result is not None:
                for member in result:
                    await message.channel.send(member.mention)
                # print(i for i in result)
            else:
                await message.channel.send('없음')
        else:
            await message.channel.send('올바르지 않은 형식입니다.')
            

def check_validate_nickname(phrases):
    nickname = phrases.split('/')
    if nickname > 2:
        return {"clan": nickname[0], "role": nickname[1], "nickname": nickname[2]}

    return None
    