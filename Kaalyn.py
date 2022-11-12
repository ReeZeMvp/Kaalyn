import discord
import json
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
Kaalyn = commands.Bot(command_prefix="k;", intents=intents ,description="working in progress")

file = open('token.json',)
data = json.load(file)

@Kaalyn.event
async def on_ready():
    print("Kaalyn UP!")
    try:
        synced = await Kaalyn.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@Kaalyn.tree.command(name="hello", description="First slash command, says hello")
async def hello (interraction: discord.Interaction):
    await interraction.response.send_message(f"Hey {interraction.user.mention}! This is a slash command!", ephemeral=True)

Kaalyn.run(data["token"])