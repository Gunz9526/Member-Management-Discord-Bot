from flask import Flask
import asyncio
from config import token

from app import app
from bot import client

# def 
#     print("1111")
#     app.run(debug=True)
#     asyncio.sleep(50)
#     client.run('')
#     print("222")

async def main_app():
    await app.run(debug=True)

async def discord_app():
    await client.start(token)

async def async_app():    
    task2 = asyncio.create_task(discord_app())
    # task1 = asyncio.create_task(main_app())
    # tasks = [task1, task2]
    # result = await asyncio.gather(*tasks)
    # return result
    await task2
    # await task1

    # loop = asyncio.get_event_loop()
    # await loop.run_in_executor(None, app.run())
    # await loop.run_in_executor(None, client.run(),'')
    # task1 = asyncio.create_task(app.run(debug=True))
    # task2 = asyncio.create_task(client.run(''))

    # await task2
    # await task1

# app.run(debug=True)
asyncio.run(async_app())