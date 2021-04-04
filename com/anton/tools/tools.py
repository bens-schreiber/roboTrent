import re

import discord
from discord.ext import commands


# File for helper functions that can be used throughout the program

# The category that temp channels are hardcoded into. Change it here.
def temp_category(t_guild: discord.Guild):
    """
    :return: ID of the temporary channels category.
    """
    if t_guild.id == 720879057469702216:
        return 827405509979013120

    return 826653009005772800


# List of strings the dad filter could activate on
g_MIN_WORD_SIZE = 3
g_DAD_REGEX = re.compile(r"\b(i'm|im|i am)\b", flags=re.IGNORECASE)


def dad_joke(t_msg: str) -> str:
    """
    Scans a message for words in the g_dad_filter.
    :param t_msg: Message to be scanned for a potential dad joke
    :return: None if no dad joke could be found, formatted string if found.
    """

    # Regex that returns a Match object if "(?i) i'm or (?i) im" is found
    dad_search: re.Match = g_DAD_REGEX.search(t_msg)

    # If a match was found
    if dad_search is not None:

        if len(t_msg) > (dad_search.end()) + g_MIN_WORD_SIZE:

            # Lol! Dad Joke!
            return f"Hi {t_msg[dad_search.end() + 1:]}, I'm Noah Jackson!"


def sus_find(t_msg: str) -> bool:
    """
    Scans a message for the word sus.
    :param t_msg: String to be scanned for the keyword "sus"
    :return: Boolean
    """

    return "sus" in t_msg.lower()


async def create_and_assign_color_role(t_hex: int, t_member: discord.Member):
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
