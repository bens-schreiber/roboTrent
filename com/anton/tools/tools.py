import discord


# File for helper functions that can be used throughout the program

async def create_and_assign_role(t_color, t_member: discord.Member):
    # The users decimal based ID
    usr_id = str(t_member.id)

    # Server the user is in
    usr_guild = t_member.guild

    # Create a new role with a color
    await usr_guild.create_role(
        name=usr_id,
        color=discord.Color(int(t_color, 16))
    )

    # Add that role to the user
    await t_member.add_roles(discord.utils.get(
        usr_guild.roles,
        name=usr_id)
    )

