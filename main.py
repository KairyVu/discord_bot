import discord
from discord.ext import commands
from discord import app_commands
import os

# Basic setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


# Events
@bot.event
async def on_ready():
    bot.tree.copy_global_to(guild=os.getenv("GUILD_ID"))
    await bot.tree.sync(guild=os.getenv("GUILD_ID"))
    # await bot.load_extension("operator_data")


@bot.event
async def on_command_error(ctx, error):
    pass

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


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_API_TOKEN"))
