import os, sys
import discord
from discord.ext import commands

from app import app

# from util.check_nickname import check_validate_nickname
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class CogAuth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='링크')
    async def send_dm(self, ctx):
        DMchannel = await ctx.author.create_dm()
        with app.app_context():
            from controller.controller_session import SessionController
            session_object = SessionController()
            tokens = session_object.create_token(discord_nickname=ctx.author.display_name, discord_id=ctx.author.name, discord_unique_id=ctx.author.id)
            embed = discord.Embed(title='링크', description='https://www.google.com')        
            embed.add_field(name='닉네임', value=(f'{ctx.author.display_name}'), inline=True)
            embed.add_field(name='아이디', value=(f'{ctx.author.name}'), inline=True)
            embed.add_field(name='고유값', value=(f'{ctx.author.id}'), inline=True)
            embed.add_field(name='Access_Token', value=(f'{tokens["access_token"]}'), inline=False)
            embed.add_field(name='Refresh_Token', value=(f'{tokens["refresh_token"]}'), inline=False)
            # embed.add_field(name='링크', value=(f"닉네임 : {ctx.author.display_name} \n유저 아이디: {ctx.author.name}\n유저 고유 아이디: {ctx.author.id}"))
            await DMchannel.send(embed=embed)
        # await DMchannel.send(f"닉네임 : {ctx.author.display_name} \n유저 아이디: {ctx.author.name}\n유저 고유 아이디: {ctx.author.id}")

async def setup(bot):
    await bot.add_cog(CogAuth(bot))
