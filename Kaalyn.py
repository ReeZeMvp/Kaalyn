import discord
import json
from discord.ext import commands

intents = discord.Intents.all()
Kaalyn = commands.Bot(command_prefix="k;", intents=intents ,description="working in progress")

@Kaalyn.event
async def on_ready():
    print("Kaalyn UP!")

file = open('token.json',)
data = json.load(file)
Kaalyn.run(data["token"])