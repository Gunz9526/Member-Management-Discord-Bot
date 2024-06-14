from flask import Flask
from bot import client
import asyncio



app = Flask(__name__)

##################################################
# import discord
# from discord.ext import commands


# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     await client.change_presence(status=discord.Status.online, activity=discord.Game('ㅎㅇ'))
#     print(f'봇 {client.user} 대기중')

# @client.event
# async def on_message(message):async def on_message(message):
    # if message.author == client.user:
    #     return

    # if message.content.startswith('!테스트'):
    #     await message.channel.send('Consider it done.')

    # if message.content.startswith('!ㅎㅇ'):
    #     DMchannel = client.create_dm(message.author)
    #     await DMchannel.send("State your will.")
####################################################

@app.route('/')
def hello_world():
    print("여기도 실행")
    return 'Hello1 World!'

@app.route('/test')
def test_field():
    return "여긴 테스트임"

# app.run(debug=True)

async def test():
    task1 = asyncio.create_task(client.start(''))
    await task1
    print("test함수")

print("되겠냐?")

asyncio.run(test())
# asyncio.run(await asyncio.create_task(test()))
print("이거 되냐?")
# asyncio.run(client.start(''))

# asyncio.run(client.start(''))
# app.run을 하므로 또 비동기함수가 호출돼서 무한 반복
# app.run이 없이 gunicorn 으로 실행 해도 되네? ㅋㅋ


# def main():    
#     asyncio.run(async_app())

# main()

# @app.route('/')
# def hello_world():
#     print("여기도 실행")
#     return 'Hello World!'

# async def async_app():
#     task1 = asyncio.create_task(app.run(debug=True))
#     task2 = asyncio.create_task(client.run(''))

#     await task2
#     await task1


# asyncio.run(client.run(''))
# print("여기까진 ㅇㅋ")

# if __name__ == '__main__':
#     app.run(debug=True)
