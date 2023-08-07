import discord
from discord.ext import commands
from discord import app_commands
import os
import operator_data
import typing
import logging


# Basic setup
logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


# Events
@bot.event
async def on_ready():
    operator_data.database = operator_data.operator_list()
    logging.info("Database is ready")
    bot.tree.copy_global_to(guild=discord.Object(id=(os.getenv("GUILD_ID"))))
    await bot.tree.sync(guild=discord.Object(id=int(os.getenv("GUILD_ID")))) 

# @bot.event
# async def on_command_error(ctx, error):
#     pass

# Commands
@bot.command()
async def avatar(ctx, member: str = None):
    if member is None:
        member = ctx.author
    elif member.startswith('<@') and member.endswith('>'):
        user_id = member[2:-1]
        member = discord.utils.get(ctx.guild.members, id=int(user_id))
    elif member.isdigit():
        member = discord.utils.get(ctx.guild.members, id=int(member))
        if not member:
            embed = discord.Embed(title="User not found", color=discord.Color.dark_blue(), description="*Please enter a valid user in the server*")
            await ctx.send(embed=embed)
            return
    else:
        embed = discord.Embed(title="Command Error", color=discord.Color.dark_blue(), description="*Use mention or user ID instead*")
        await ctx.send(embed=embed)
        return

    try:
        avatar_url = member.avatar.url
    except:
        file = discord.File(r"C:\Users\khoid\OneDrive\Desktop\disimg.png")
        embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.dark_blue())
        embed.set_image(url=f"attachment://{file.filename}")
        await ctx.send(embed=embed, file=file)
        return
    
    embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.dark_blue())
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)


@bot.tree.command()
async def operator(interaction: discord.Interaction, *, operator: str, skill: int):
    skill_brief, text1, text2, text3, text4, text5, url = operator_data.skill_search(operator, skill)
    embed = discord.Embed(title=f"{operator.title()}'s Skill {skill}", color=discord.Color.dark_blue())
    embed.add_field(name="", value=f"{skill_brief}", inline=False)
    if text1 is None:
        pass
    else:
        embed.add_field(name="", value=f"{text1}", inline=False)
        embed.add_field(name="", value=f"{text2}", inline=False)
        embed.add_field(name="", value=f"{text3}", inline=False)
        embed.add_field(name="", value=f"{text4}", inline=False)
        embed.add_field(name="", value=f"{text5}", inline=False)

    if url is not None:
        embed.set_thumbnail(url=url)
    await interaction.response.send_message(embed=embed)


@operator.autocomplete("operator")
async def operator(interaction: discord.Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
    data = []
    for partial in operator_data.database:
        if current.lower() in partial.lower():
            data.append(app_commands.Choice(name=partial, value=partial))
    return data

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_API_TOKEN"))