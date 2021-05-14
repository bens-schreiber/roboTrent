from discord.ext import commands
from com.anton.tools.tools import *

#######################
# VOICE COMMANDS ONLY #
#######################
from com.anton.tools.tools import temp_category

g_CATEGORY_LIMIT = 10


class VoiceCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    @commands.command(aliases=["mkc", "channel"])
    async def make_temporary_channel(self,
                                     t_ctx: discord.ext.commands.Context,
                                     t_name: str = "temp-channel",
                                     t_limit=0,
                                     ):
        guild: discord.Guild = t_ctx.guild
        category: discord.CategoryChannel = discord.utils.get(guild.categories, id=temp_category(t_ctx.guild))

        # Check to see if the temp category channel is at its limit
        if len(category.channels) <= g_CATEGORY_LIMIT:
            await guild.create_voice_channel(category=category,
                                             name=t_name,
                                             user_limit=abs(t_limit) if abs(t_limit) < 100 else 99,
                                             )
            await send_success_embed(t_ctx, t_title=f"Created channel: {t_name}")

        else:
            await send_error_embed(t_ctx, t_description="Maximum channels reached")

    @commands.command(name="limit")
    async def edit_temp_channel_limit(self, t_ctx: discord.ext.commands.Context, t_limit: int):
        if t_ctx.author.voice is not None:
            channel: discord.VoiceChannel = t_ctx.author.voice.channel

            if channel.category_id == temp_category(t_ctx.guild):
                await channel.edit(user_limit=abs(t_limit) if abs(t_limit) < 100 else 99)
                await send_success_embed(t_ctx, t_description=f"Increased {channel} limit to {t_limit}")

            else:
                await send_error_embed(t_ctx, t_description="Can't edit this channel")

        else:
            await send_error_embed(t_ctx, t_description="Must be in a voice channel")

    @commands.command(name="name")
    async def edit_temp_channel_name(self, t_ctx: discord.ext.commands.Context, t_name):
        if t_ctx.author.voice is not None:
            channel: discord.VoiceChannel = t_ctx.author.voice.channel

            if channel.category_id == temp_category(t_ctx.guild):
                await send_success_embed(t_ctx, t_description=f"Changed {channel.name} name to {t_name}")
                await channel.edit(name=t_name)

            else:
                await send_error_embed(t_ctx, t_description="Can't edit this channel")

        else:
            await send_error_embed(t_ctx, t_description="Must be in a voice channel")


def setup(bot):
    bot.add_cog(VoiceCommand(bot))
