import re
import sys
import traceback

from discord.ext import commands
from com.anton.tools.tools import *

# Change this to YOUR prefix!!
g_client = commands.Bot(command_prefix=">")

# Make sure to change this to YOUR bot token!!!
g_TOKEN = ""

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
    # Make sure the message isn't sent from the bot.
    if not t_msg.author.bot:
        # Channel msg was sent in
        channel: discord.TextChannel = t_msg.channel

        # Try to find a dad joke
        joke = dad_joke(t_msg.content)
        if joke:
            await channel.send(joke)

        if sus_find(t_msg.content):
            await channel.send("you said sus")

    await g_client.process_commands(t_msg)


@g_client.event
async def on_voice_state_update(t_member: discord.Member, t_before, t_after: discord.VoiceState):
    # get channel
    if t_before.channel is not None:
        channel: discord.VoiceChannel = t_before.channel

        # If the category is in the temporary channels category
        if channel.category_id == temp_category():

            # Delete channel if no members
            if len(channel.members) == 0:
                await channel.delete()


@g_client.event
async def on_member_join(t_member: discord.Member):
    # Default to white hex code
    await create_and_assign_role(0xFFFFFF, t_member)


# Handle any errors
@g_client.event
async def on_command_error(t_ctx: discord.ext.commands.Context, t_error: discord.ext.commands.CommandError):
    if hasattr(t_ctx.command, "on_error"):
        return

    # Anything in ignored will return and prevent anything happening.
    if isinstance(t_error, commands.CommandNotFound):
        await send_error_embed(t_ctx, t_description="Command not found")

    if isinstance(t_error, commands.MissingRequiredArgument):
        await send_error_embed(t_ctx, t_description="Missing required arguments.")

    if isinstance(t_error, commands.BadArgument):
        await send_error_embed(t_ctx, t_description="Bad arguments.")

    else:
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print('Ignoring exception in command {}:'.format(t_ctx.command), file=sys.stderr)
        traceback.print_exception(type(t_error), t_error, t_error.__traceback__, file=sys.stderr)


g_client.run(g_TOKEN)
