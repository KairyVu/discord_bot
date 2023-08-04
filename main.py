import discord
from discord.ext import commands
from discord import app_commands
import os

# Basic setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


# Commands
@bot.event
async def on_command_error(ctx, error):
    pass

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    avatar_url = member.avatar.url

    embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.dark_blue())
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_API_TOKEN"))
