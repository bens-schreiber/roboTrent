import discord
from discord.ext import commands


class VoiceCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    #put some voice commands here?? maybe??


def setup(bot):
    bot.add_cog(VoiceCommand(bot))