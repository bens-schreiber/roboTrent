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
