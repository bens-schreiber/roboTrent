import sys
import traceback

import discord
from discord.ext import commands
from com.anton.tools.tools import *

# Change this to YOUR prefix!!
g_client = commands.Bot(command_prefix=">")

# Make sure to change this to YOUR bot token!!!
g_TOKEN = "ODI2MjgwNjQ3NjgxMTE0MTQy.YGKL0Q.qKgFd8SOAPIdaKrqsB_kOECt3Yw"

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
        await ctx.send("you said it!")

    await g_client.process_commands(t_msg)


@g_client.event
async def on_member_join(t_member: discord.Member):
    await create_and_assign_role(0xFFFFFF, t_member)


# Handle any errors
@g_client.event
async def on_command_error(t_ctx: discord.ext.commands.Context, t_error: discord.ext.commands.CommandError):
    if hasattr(t_ctx.command, 'on_error'):
        return

    # Anything in ignored will return and prevent anything happening.
    if isinstance(t_error, commands.CommandNotFound):
        await t_ctx.send(embed=ErrorEmbed(t_description="Command not found").embed())

    else:
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print('Ignoring exception in command {}:'.format(t_ctx.command), file=sys.stderr)
        traceback.print_exception(type(t_error), t_error, t_error.__traceback__, file=sys.stderr)


g_client.run(g_TOKEN)
