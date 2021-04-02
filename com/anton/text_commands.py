from random import randint

from discord.ext import commands
from com.anton.tools.tools import *


######################
# TEXT COMMANDS ONLY #
######################

class TextCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    # Change the color of a user's designated color role. Color roles are named after their static ID's.
    @commands.command(aliases=["colorme", "color", "clr"])
    async def color_member_role(self, t_ctx: discord.ext.commands.Context, t_color):
        """"
        :param t_ctx: Context
        :param t_color: Hex color code
        """
        try:
            # Convert color input to a hex num. If not a possible hex value (larger than 16777215)
            # fill, make white. Throws ValueError if impossible
            hex_color = int(t_color, 16) if int(t_color, 16) <= 0xFFFFFF else 0xFFFFFF

            has_role = False
            for role in t_ctx.author.roles[1:]:  # Skip first role in role list w/ slicing, its always @everyone
                # if the color role is present, edit it
                if role.name == "color":
                    has_role = True
                    await role.edit(color=discord.Color(hex_color))
                    break

            # If the user does not have a color role already defined, make one
            if not has_role:
                # See implementation in tools
                await create_and_assign_color_role(hex_color, t_ctx.author)

            await send_success_embed(t_ctx, t_title=f"Color changed to {t_color}")

        except ValueError:
            await send_error_embed(t_ctx, t_description="Must be a hex value")

    @commands.command(aliases=["avatar", "pfp"])
    async def send_avatar(self, t_ctx: discord.ext.commands.Context, t_member: discord.Member = None):
        """
        :param t_ctx: Context
        :param t_member: Optional member to grab avatar from. Defaults to the author.
        """
        await t_ctx.send(t_member.avatar_url if t_member else t_ctx.author.avatar_url)

    @commands.command(aliases=["massping", "mp"])
    @commands.cooldown(1, 120)
    async def ping_user_random(self, t_ctx: discord.ext.commands.Context, t_member: discord.Member = None):
        """
        :param t_ctx: Context
        :param t_member: Optional member to ping. Defaults to the author.
        """
        for ping in range(randint(1, 5)):
            await t_ctx.send(t_member.mention if t_member else t_ctx.author.mention)

    @commands.command(aliases=["embedme", "embed"])
    async def embed_user_message(self, t_ctx: discord.ext.commands.Context,
                                 t_title: str = "Random color!!",
                                 t_description: str = None,
                                 t_color: str = None):

        try:
            # Try to convert to a hex num. If the hex num wasn't specified (NONE), give it a random color.
            hex_value = int(t_color, 16) if t_color is not None else discord.Color.random().value
            await t_ctx.send(embed=discord.embeds.Embed(title=t_title,
                                                        description=t_description,
                                                        color=hex))
        except ValueError:
            await send_error_embed(t_ctx, t_description="Must be a hex value")


def setup(bot):
    bot.add_cog(TextCommand(bot))
