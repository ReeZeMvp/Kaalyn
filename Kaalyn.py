import discord
import json
from discord.ext import commands

Kaalyn = commands.Bot(command_prefix="k;", description="working in progress")

file = open('token.json',)
data = json.load(file)
Kaalyn.run(data["token"])