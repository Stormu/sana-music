import discord
from discord.ext import commands

class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    #Test command to remember how to even use discord.py
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(f'Hello {member.name}~')

async def setup(bot) -> None:
    await bot.add_cog(General(bot))