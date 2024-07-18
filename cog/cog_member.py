import discord
from discord.ext import commands
from util.check_nickname import check_validate_nickname

class CogMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='클랜원추가')
    async def add_clan_member(self, ctx, *args):
        from app import app
        with app.app_context():
            from controller.controller_member import MemberController
            member_object = MemberController()
            clan_name = check_validate_nickname(ctx.author.display_name)

            clan_id = member_object.retrieve_clan_id(clan_name['clan'])
            for arg in args:
                member_object.add_clan_member(clan_id=clan_id, nickname=arg)

        await ctx.channel.send(clan_name['clan'] + '클랜에 ' + ', '.join(args) + '이 추가되었습니다.', reference=ctx.message)

    @commands.command(name='클랜원검색')
    async def retrieve_member(self, ctx, args):
        from app import app
        with app.app_context():
            from controller.controller_member import MemberController
            member_object = MemberController()
            clan_name = check_validate_nickname(ctx.author.display_name)
            clan_id = member_object.retrieve_clan_id(clan_name['clan'])
            member_list = member_object.retrieve_clan_member(nickname=args, clan_id=clan_id)

            embed = discord.Embed(title='클랜원 목록', description=f'{clan_name["clan"]}클랜의 검색된 클랜 멤버 입니다.')        
            embed.add_field(name=f'멤버 ( {len(member_list)}명 )', value='\n'.join(member_list), inline=False)
            await ctx.channel.send(embed=embed, reference=ctx.message)

    @commands.command(name='블랙리스트검색')
    async def retrieve_blacklist(self, ctx, args):
        from app import app
        with app.app_context():
            from controller.controller_member import MemberController
            member_object = MemberController()
            member_list = member_object.retrieve_blacklist(nickname=args)

            embed = discord.Embed(title='블랙리스트')
            embed.add_field(name=f'멤버 ( {len(member_list)}명 )', value='\n'.join(member_list), inline=False)
            await ctx.channel.send(embed=embed, reference=ctx.message)

async def setup(bot):
    await bot.add_cog(CogMember(bot))
