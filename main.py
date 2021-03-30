import discord
from discord.ext import commands
import text_commands

# Change this to YOUR prefix!!
g_client = commands.Bot(command_prefix=">")

# Make sure to change this to YOUR bot token!!!
g_token = "ODI2MjgwNjQ3NjgxMTE0MTQy.YGKL0Q.F2nhLzEDOevY6PdKXYHfwg32k4w"

# Here we are going to load our cogs
initial_extensions = [
    "text_commands",
    "voice_commands"
]

if __name__ == '__main__':
    for extension in initial_extensions:
        g_client.load_extension(extension)


#######################
# EVENTS ONLY IN MAIN #
#######################

# Don't fuck with the on_ready method.
# It is apparently recommended not to do shit in it.
@g_client.event
async def on_ready():
    print("online")


@g_client.event
async def on_message(t_msg: discord.Message):
    ctx = t_msg.channel
    if "sus" in t_msg.content:
        await ctx.send(t_msg.content)

    await g_client.process_commands(t_msg)


g_client.run(g_token)
