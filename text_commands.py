import discord
from discord.ext import commands


class TextCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    @commands.command(name="hi")
    async def respond_with_hi(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send("hi!")


def setup(bot):
    bot.add_cog(TextCommand(bot))
