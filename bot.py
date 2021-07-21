import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX")

client = commands.Bot(command_prefix=PREFIX)

client.remove_command("help")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="Welcome channel name")
    await channel.send(f"{member.mention} has just joined the server!")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="Leave channel name")
    await channel.send(f"{member.mention} has left the server.")

client.run(TOKEN)