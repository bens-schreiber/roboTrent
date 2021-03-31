import discord
from discord.ext import commands


# File for helper functions that can be used throughout the program

async def create_and_assign_role(t_hex: int, t_member: discord.Member):
    """
    :param t_hex: integer hex color code
    :param t_member: member that should be assigned the role
    :return:
    """

    # Server the user is in
    usr_guild = t_member.guild

    # Create a new role with a color
    role = await usr_guild.create_role(
        name="color",
        color=discord.Color(t_hex)
    )

    # Add that role to the user
    await t_member.add_roles(role)


async def send_error_embed(t_ctx: discord.ext.commands.Context,
                           t_title="Error",
                           t_description="An error occurred :(",
                           t_color=0xff0000
                           ):
    await t_ctx.send(embed=discord.Embed(title=t_title, description=t_description, color=t_color))


async def send_success_embed(t_ctx: discord.ext.commands.Context,
                             t_title="Success",
                             t_description="",
                             t_color=0x00ff00
                             ):

    await t_ctx.send(embed=discord.Embed(title=t_title, description=t_description, color=t_color))