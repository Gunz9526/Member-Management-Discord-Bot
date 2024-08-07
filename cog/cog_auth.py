import os, sys
import discord
from discord.ext import commands

from app import app
from config import link_url

# from util.check_nickname import check_validate_nickname
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class CogAuth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # DM채널일 경우 서버 내 닉네임 추적
    @commands.command(name='링크')
    async def send_dm(self, ctx):
        DMchannel = await ctx.author.create_dm()

        # 봇이 속한 길드는 1개이므로
        for guild in self.bot.guilds:
            member = await guild.query_members(user_ids=ctx.author.id)

        with app.app_context():
            from controller.controller_session import SessionController
            session_object = SessionController()
            tokens = session_object.create_token(discord_nickname=ctx.author.display_name, discord_id=ctx.author.name, discord_unique_id=ctx.author.id)
            sessions = session_object.create_session(discord_nickname=ctx.author.display_name, discord_id=ctx.author.name, discord_unique_id=ctx.author.id, access_token=tokens['access_token'])
            embed = discord.Embed(title='링크', description=link_url+'/#/session/'+sessions['session_name'])
            embed.add_field(name='닉네임', value=(f'{member[0].nick}'), inline=True)
            embed.add_field(name='아이디', value=(f'{ctx.author.name}'), inline=True)
            embed.add_field(name='고유값', value=(f'{ctx.author.id}'), inline=True)
            embed.add_field(name='Access_Token', value=(f'{tokens["access_token"]}'), inline=False)
            embed.add_field(name='session_name', value=(f'{sessions["session_name"]}'), inline=False)
            await DMchannel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CogAuth(bot))
