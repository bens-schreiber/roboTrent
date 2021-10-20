import sys
import traceback

from discord.ext import commands
from com.anton.tools.tools import *

# Change this to YOUR prefix!!
g_client = commands.Bot(command_prefix=["RoboTrent ", "robotrent ", "Robotrent "])
g_client.remove_command("help")

g_GENERAL_CHANNEL = 899684495337328655
g_BOT_CHANNEL = 900413299894673438

g_DAD_JOKE_ALLOWED = [g_GENERAL_CHANNEL, g_BOT_CHANNEL]

# bot token
g_TOKEN = "OTAwMjQxNTY3ODY3MTA1MzAw.YW-dSw.jwIEAW2x2wqUGDDfp-3Bn5E8ktw"

# Here we are going to load our cogs ( other .py scripts )
initial_extensions = [
    "text_commands"
]

if __name__ == '__main__':
    for extension in initial_extensions:
        g_client.load_extension(extension)


#######################
# EVENTS ONLY IN MAIN #
#######################

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
        joke = await dad_joke(t_msg.content)
        if channel.id in g_DAD_JOKE_ALLOWED and joke:
            await channel.send(joke)

        elif await gaming_find(t_msg.content):
            await channel.send("gaming")

    await g_client.process_commands(t_msg)


# Handle any errors
@g_client.event
async def on_command_error(t_ctx: discord.ext.commands.Context, t_error: discord.ext.commands.CommandError):
    if hasattr(t_ctx.command, "on_error"):
        return

    if isinstance(t_error, commands.MissingRequiredArgument):
        await send_error_embed(t_ctx, t_description="Missing required arguments.")

    if isinstance(t_error, commands.BadArgument):
        await send_error_embed(t_ctx, t_description="Bad arguments.")

    if isinstance(t_error, commands.CommandOnCooldown):
        await t_ctx.send("Slow your roll buddy, wait a while.")

    else:
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print('Ignoring exception in command {}:'.format(t_ctx.command), file=sys.stderr)
        traceback.print_exception(type(t_error), t_error, t_error.__traceback__, file=sys.stderr)


g_client.run(g_TOKEN)
