import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print("Bot is online and ready!")

@bot.event
async def on_ready():
    print("Bot is online and ready!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

import os
bot.run(os.getenv("DISCORD_TOKEN"))


