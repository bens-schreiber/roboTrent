from discord.ext import commands

from com.anton.tools.tools import *


######################
# TEXT COMMANDS ONLY #
######################

g_BOT_CHANNEL = 900413299894673438

class TextCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    @commands.command(aliases=["avatar", "pfp"])
    async def send_avatar(self, t_ctx: discord.ext.commands.Context, t_member: discord.Member = None):
        """
        :param t_ctx: Context
        :param t_member: Optional member to grab avatar from. Defaults to the author.
        """
        await t_ctx.send(t_member.avatar_url if t_member else t_ctx.author.avatar_url)

    @commands.command(name="tront")
    async def send_tront(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send("tront")

    @commands.command(name="youtube")
    async def send_youtube(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send("https://www.youtube.com/c/TrentLenkarski")

    @commands.command(name="help")
    async def help_command(self, t_ctx: discord.ext.commands.Context):
        if t_ctx.channel.id == g_BOT_CHANNEL:
            await send_success_embed(t_ctx, t_title="Commands", t_description="""
            - help: 
                displays this message
                
            - tront
                sends some tront
                
            - youtube
                sends some trent youtube
                
            - avatar 
                params: [optional: @Member] 
                desc: shows the avatar of yourself, or a member
                
            Active Listening Commands:
            - will make a hilarious dad joke when you start a phrase with "i'm" in #general or #bot
            
            """)


def setup(bot):
    bot.add_cog(TextCommand(bot))
