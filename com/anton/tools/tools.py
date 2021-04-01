import re

import discord
from discord.ext import commands


# File for helper functions that can be used throughout the program

# The category that temp channels are hardcoded into. Change it here.
def temp_category():
    """
    :return: ID of the temporary channels category.
    """
    return 826653009005772800


# List of strings the dad filter could activate on
g_dad_filter = ["im", "i'm", "Im", "I'm", "IM", "I'M"]


def dad_joke(t_msg: str) -> str:
    """
    :param t_msg: Message to be scanned for a potential dad joke
    :return: None if no dad joke could be found, formatted string if found.
    """
    # Search every word of the message to see if it contains I'm
    for word in g_dad_filter:

        # Regex that returns a Match object if "I'm" is found
        dad_search: re.Match = re.search(r'\b' + re.escape(word) + r'\b', t_msg)

        # If a match was found
        if dad_search is not None:

            # Lol! Dad Joke!
            return f"Hi {t_msg[dad_search.end() + 1:]}, I'm Dad!"


def sus_find(t_msg: str) -> bool:
    """
    :param t_msg: String to be scanned for the keyword "sus"
    :return: Boolean
    """

    return "sus" in t_msg.lower()


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
                             t_title="",
                             t_description="",
                             t_color=0x00ff00
                             ):
    await t_ctx.send(embed=discord.Embed(title=t_title, description=t_description, color=t_color))
