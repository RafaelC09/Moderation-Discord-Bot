from discord.ext import commands
import discord
import asyncio

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ticket(self, ctx):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }
        
        channel = await guild.create_text_channel(f"ticket-{ctx.author.name}", overwrites=overwrites)
        await channel.send(f"{ctx.author.mention}, describe here your problem.")
        
    @commands.command()
    async def close(self, ctx):
        await ctx.send("The channel will be deleted in 5 seconds...")
        await asyncio.sleep(5)
        await ctx.channel.delete()
        
async def setup(bot):
    await bot.add_cog(Tickets(bot))