import discord
from discord.ext import commands
# from controller.controller_member import MemberController # 이 부분은 외부에 있다고 가정합니다.

class MemberCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='링크')
    async def send_link(self, ctx):
        DMchannel = await ctx.author.create_dm()
        nickname = ctx.author.display_name.split('/')
        if len(nickname) > 2:
            await DMchannel.send("반갑습니다. " + nickname[0] + " 클랜의 " + nickname[2] + " " + nickname[1] + "님")
        else:
            await DMchannel.send("반갑습니다. " + ctx.author.display_name + "님 닉네임을 형식에 맞게 변경해주세요")

    @commands.command(name='멤버추가')
    async def add_member(self, ctx, *, member_info=None):
        if member_info:
            add_user = self.check_validate_nickname(member_info)
            if add_user:
                await ctx.send('멤버 ' + add_user['nickname'], reference=ctx.message)
            else:
                await ctx.send('추가 할 멤버를 정확히 입력해주세요', reference=ctx.message)
        else:
            await ctx.send('추가 할 멤버를 정확히 입력해주세요', reference=ctx.message)

    @commands.command(name='멤버검색')
    async def search_member(self, ctx, *, query=None):
        if query:
            result = await ctx.guild.query_members(query)
            if result:
                for member in result:
                    await ctx.send(member.mention, reference=ctx.message)
            else:
                await ctx.send('없음', reference=ctx.message)
        else:
            await ctx.send('올바르지 않은 형식입니다.', reference=ctx.message)

    @commands.command(name='클랜원추가')
    async def add_clan_member(self, ctx, *, member_info=None):
        if member_info:
            from controller.controller_member import MemberController
            member_object = MemberController()
            nickname = ctx.author.display_name.split('/')
            
            clan_id = member_object.retrive_clan_id(nickname[0])
            member_object.add_clan_member(clan_id=clan_id, nickname=member_info)
            await ctx.send(nickname[0] + '클랜에 ' + member_info + '이 추가되었습니다.', reference=ctx.message)
        else:
            await ctx.send('추가 할 멤버 정보를 입력해주세요', reference=ctx.message)

    def check_validate_nickname(self, phrases):
        nickname = phrases.split('/')
        if len(nickname) > 2:
            return {"clan": nickname[0], "role": nickname[1], "nickname": nickname[2]}
        return None
