from discord.ext import commands
import discord

# You can add some events here

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
async def setup(bot):
    await bot.add_cog(Messages(bot))