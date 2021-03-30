import discord
from discord.ext import commands
from com.anton.tools.tools import *


######################
# TEXT COMMANDS ONLY #
######################

class TextCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    # Change the color of a user's designated color role. Color roles are named after their static ID's.
    @commands.command(name="colorme")
    async def color_member_role(self, t_ctx: discord.ext.commands.Context, t_color):

        try:

            hex_color = int(t_color, 16)  # Convert color input to a hex num. Could throw ValueError

            # Iterate through roles to find color role.
            has_role = False
            for role in t_ctx.author.roles[1:]:  # Skip first role in role list w/ slicing, its always @everyone
                if role.name == "color":
                    has_role = True
                    await role.edit(color=discord.Color(hex_color))
                    break

            # If the user does not have a color role already defined, make one
            if not has_role:
                # See implementation in tools
                await create_and_assign_role(hex_color, t_ctx.author)

            await t_ctx.send(embed=SuccessEmbed(t_title=f"Color changed to {t_color}").embed())

        except ValueError:
            await t_ctx.send(embed=ErrorEmbed(t_description="Must be a hex value.").embed())

    @commands.command(name="avatar")
    async def send_avatar(self, t_ctx: discord.ext.commands.Context, t_member: discord.Member = None):

        if t_member:

            await t_ctx.send(t_member.avatar_url)

        else:

            await t_ctx.send(t_ctx.author.avatar_url)


def setup(bot):
    bot.add_cog(TextCommand(bot))
