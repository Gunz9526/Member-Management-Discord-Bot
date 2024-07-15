import threading

from config import token

from app import app
from bot import bot

# def flask_app_init():
#     if __name__ == '__main__':
#         app.run(debug=True)

# shared_data = {}

def discord_bot_init():
    bot.run(token)

def initialize():
    discord_thread = threading.Thread(target=discord_bot_init)
    discord_thread.daemon = True

    discord_thread.start()

    for thread in threading.enumerate():
        print('***', thread.name)

    return app
