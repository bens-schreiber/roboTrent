import re

import discord
from discord.ext import commands

# List of strings the dad filter could activate on
g_MIN_WORD_SIZE = 3
g_DAD_REGEX = re.compile(r"\b(i'm|im|i am)\b", flags=re.IGNORECASE)
g_GAMING_REGEX = re.compile(r"\b(gaming)\b", flags=re.IGNORECASE)


async def dad_joke(t_msg: str) -> str:
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
            return f"Hi {t_msg[dad_search.end() + 1:]}, I'm Trent!"


async def gaming_find(t_msg: str) -> bool:
    """
    Scans a message for the word gaming.
    :param t_msg: String to be scanned for the keyword "gaming"
    :return: Boolean
    """

    return g_GAMING_REGEX.search(t_msg) is not None


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
