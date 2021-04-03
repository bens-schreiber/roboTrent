from random import randint

from discord.ext import commands
from com.anton.tools.tools import *
from webcolors import name_to_hex


######################
# TEXT COMMANDS ONLY #
######################

class TextCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    # Change the color of a user's designated color role. Color roles are named after their static ID's.
    @commands.command(aliases=["colorme", "color", "clr"])
    async def color_member_role(self, t_ctx: discord.ext.commands.Context, t_color):
        """"
        :param t_ctx: Context
        :param t_color: Hex color code
        """
        try:
            # Attempt to convert the value of inputted color to a hex value from the name_to_hex web colors function.
            # Throws value error if the value could not be found from the color
            hex_color = int(name_to_hex(t_color)[1:], 16)  # Start at the first index because web color adds hash

        except ValueError:
            try:
                # Convert color input to a hex num. If not a possible hex value (larger than 16777215)
                # fill, make white. Throws ValueError if impossible
                hex_color = int(t_color, 16) if int(t_color, 16) <= 0xFFFFFF else 0xFFFFFF

            except ValueError:
                hex_color = discord.Color.random().value  # Give it a random hex value.
                t_color = "Random Color, could not find matching name."

        has_role = False
        for role in t_ctx.author.roles[1:]:  # Skip first role in role list w/ slicing, its always @everyone
            # if the color role is present, edit it
            if role.name == "color":
                has_role = True
                await role.edit(color=discord.Color(hex_color))
                break

        # If the user does not have a color role already defined, make one
        if not has_role:
            # See implementation in tools
            await create_and_assign_color_role(hex_color, t_ctx.author)

        await send_success_embed(t_ctx, t_description=f"Color changed to {t_color}")

    @commands.command(name="colors")
    async def send_available_colors(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send("""
                         https://cdn.discordapp.com/attachments/826270722854748184/827387186932351016/0i79GSEuYp0ARo75g.png
                         """)

    @commands.command(aliases=["avatar", "pfp"])
    async def send_avatar(self, t_ctx: discord.ext.commands.Context, t_member: discord.Member = None):
        """
        :param t_ctx: Context
        :param t_member: Optional member to grab avatar from. Defaults to the author.
        """
        await t_ctx.send(t_member.avatar_url if t_member else t_ctx.author.avatar_url)

    @commands.command(aliases=["massping", "mp"])
    @commands.cooldown(1, 120)
    async def ping_user_random(self, t_ctx: discord.ext.commands.Context, t_member: discord.Member = None):
        """
        :param t_ctx: Context
        :param t_member: Optional member to ping. Defaults to the author.
        """
        for ping in range(randint(1, 5)):
            await t_ctx.send(t_member.mention if t_member else t_ctx.author.mention)

    @commands.command(aliases=["embedme", "embed"])
    async def embed_user_message(self, t_ctx: discord.ext.commands.Context,
                                 t_title: str = "Random color!!",
                                 t_description: str = None,
                                 t_color: str = None):

        try:
            # Try to convert to a hex num. If the hex num wasn't specified (NONE), give it a random color.
            hex_value = int(t_color, 16) if t_color is not None else discord.Color.random().value
            await t_ctx.message.delete()
            await t_ctx.send(embed=discord.embeds.Embed(title=t_title,
                                                        description=t_description,
                                                        color=hex_value))
        except ValueError:
            await send_error_embed(t_ctx, t_description="Must be a hex value")

    @commands.command(aliases=["asteve", "aryansteve"])
    async def send_aryan_steve(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send("https://cdn.discordapp.com/attachments/826271209930096671/827603602914279494"
                         "/6615pRbr369cIbiCN32_EPUtwJi7HW_2WscrZoxwYGJMsP0xIuhh5a8qJ3r34UFNnL3pKuPKu_pOEM07-jSZs500"
                         ".png")

    @commands.command(name="help")
    async def help_command(self, t_ctx: discord.ext.commands.Context):
        await send_success_embed(t_ctx, t_title="Commands", t_description="""
        - help: 
            displays this message
            
        - avatar 
            params: [optional: @Member] 
            desc: shows the avatar of yourself, or a member
            
        - colorme, color, clr
          params: [color]
          desc: gives you a role of that hex color OR color name.
          
        - massping, mp 
            params: [optional: @Member]
            desc: pings a member 1-5 times on a 2 minute cooldown
            
        - embedme, embed
            params: [optional: title, optional: description, optional: color]
            desc: embeds a message. Random color if not specified
        
        - channel, mkc
            params: [optional: name, optional: limit]
            desc: creates a temporary channel that gets deleted when at 0 members.
        
        - limit
            params: [limit]
            desc: edits the temporary channel you are in
        
        - name
            params: [name]
            desc: edits the temporary channel you are in
        
        - aryansteve, asteve
            desc: displays aryan steve
            
        Active Listening Commands:
        - will call you out for saying "sus"
        - will make a hilarious dad joke when you say "i'm"
        
        COLORS:
        https://cdn.discordapp.com/attachments/826270722854748184/827387186932351016/0i79GSEuYp0ARo75g.png
        """)


def setup(bot):
    bot.add_cog(TextCommand(bot))
