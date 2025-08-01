from discord.ext import commands
from discord.ui import Button, View
import discord

class RoomsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Room 1", style=discord.ButtonStyle.success, custom_id="room1", row=0)
    async def room1_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("You joined Room 1!", ephemeral=True)
        
    @discord.ui.button(label="Room 2", style=discord.ButtonStyle.success, custom_id="room2", row=0)
    async def room2_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("You joined Room 2!", ephemeral=True)
        
    @discord.ui.button(label="Room 3", style=discord.ButtonStyle.success, custom_id="room3", row=0)
    async def room3_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("You joined Room 3!", ephemeral=True)

class Elo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def elo(self, ctx):
        embed = discord.Embed(
            title="ELO",
            description="",
            color=0xadd8e6
        )
        embed.set_author(name="Simple BOT", url=None)
        embed.set_footer(text="This bot is only an example used for learning some notions of programming.")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def joinelo(self,ctx):
        embed = discord.Embed(
            title="ELO's rooms",
            description="__**Room 1**__: (0/6)\n__**Room 2**__: (0/6)\n__**Room 3**__: (0/6)",
            color=0xadd8e6
        )
        embed.set_author(name="Simple BOT", url=None)
        await ctx.send(embed=embed, view=RoomsView())
        
async def setup(bot):
    await bot.add_cog(Elo(bot))