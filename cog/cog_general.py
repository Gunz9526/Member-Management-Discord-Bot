import discord
from discord.ext import commands
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class CogGeneral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='도움')
    async def request_help(self, ctx):
        embed = discord.Embed(title='명령어', description='명령어들의 모음입니다.')
        embed.add_field(name='!링크', value='클랜원 및 블랙리스트 작업이 가능한 링크가 DM으로 전송됩니다.')
        embed.add_field(name='!서버이름', value='현재는 서버이름만 출력. 추후 서버ID기반으로 작업가능')
        embed.add_field(name='!멤버검색', value='해당 문자열이 포함된 디스코드 사용자 검색. 클랜 검색으로 이용할 예정')        
        embed.add_field(name='!멤버추가', value='간단한 클랜원 추가는 이 명령어로 할 수 있도록 시도할 에정')
        await ctx.channel.send(embed=embed, reference=ctx.message)

    @commands.command(name='서버이름')
    async def request_servername(self, ctx):
        await ctx.channel.send(ctx.guild.name + ' ' + str(ctx.guild.id), reference=ctx.message)


async def setup(bot):
    await bot.add_cog(CogGeneral(bot))
