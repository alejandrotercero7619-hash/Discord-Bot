import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Tus IDs guardados
GUILD_ID = 1544494903411740793
OWNER_ID = 778481723666333707

@bot.event
async def on_ready():
    print(f"¡Conectado como {bot.user}!")

bot.run(os.getenv('DISCORD_TOKEN')
