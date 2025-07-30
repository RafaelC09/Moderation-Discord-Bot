import discord
from discord.ext import commands
import config
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    
async def setup():
    await bot.load_extension('cogs.moderation')
    await bot.load_extension('cogs.messages')
    await bot.load_extension('cogs.tickets')
    
    await bot.start(config.TOKEN)

asyncio.run(setup())