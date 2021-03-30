import discord
from discord.ext import commands


######################
# TEXT COMMANDS ONLY #
######################

class TextCommand(commands.Cog):
    def __init__(self, m_bot):
        self.m_bot = m_bot

    @commands.command(name="hi")
    async def respond_with_hi(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send("hi!")

    # Change the color of a user's designated color role. Color roles are named after their static ID's.
    @commands.command(name="colorme")
    async def color_member_role(self, t_ctx: discord.ext.commands.Context, t_color):

        # 6 is max hex color size
        if len(t_color) < 7:

            # The users decimal based ID
            usr_id = str(t_ctx.author.id)

            # If the color role already exists, edit the color
            if discord.utils.get(t_ctx.guild.roles, name=usr_id):

                role = discord.utils.get(t_ctx.guild.roles, name=usr_id)

                await role.edit(color=discord.Color(int(t_color, 16)))

            # If the user does not already have a colored role, create one
            else:

                # Create a new role with the updated color
                await t_ctx.guild.create_role(
                    name=usr_id,
                    color=discord.Color(int(t_color, 16))
                )

                # Add that role to the user
                await t_ctx.message.author.add_roles(discord.utils.get(
                    t_ctx.guild.roles,
                    name=usr_id)
                )

        else:

            await t_ctx.send("Incomprehensible. ")

    @commands.command(name="test")
    async def test(self, t_ctx: discord.ext.commands.Context):
        await t_ctx.send(t_ctx.author.id)

        
def setup(bot):
    bot.add_cog(TextCommand(bot))
