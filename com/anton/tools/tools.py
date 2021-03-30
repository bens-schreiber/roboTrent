import discord


# File for helper functions that can be used throughout the program

async def create_and_assign_role(t_hex: int, t_member: discord.Member):
    # Server the user is in
    usr_guild = t_member.guild

    # Create a new role with a color
    role = await usr_guild.create_role(
        name="color",
        color=discord.Color(t_hex)
    )

    # Add that role to the user
    await t_member.add_roles(role)


class ErrorEmbed:
    def __init__(self,
                 t_title="Error",
                 t_description="You've Done it, an Error!",
                 t_color=0xff0000
                 ):
        self.t_title = t_title
        self.t_description = t_description
        self.t_color = t_color

    def embed(self) -> discord.Embed:
        return discord.Embed(title=self.t_title,
                             description=self.t_description,
                             color=self.t_color)


class SuccessEmbed:
    def __init__(self,
                 t_title="Successful",
                 t_description="",
                 t_color=0x00ff00
                 ):
        self.t_title = t_title
        self.t_description = t_description
        self.t_color = t_color

    def embed(self) -> discord.Embed:
        return discord.Embed(title=self.t_title,
                             description=self.t_description,
                             color=self.t_color)
