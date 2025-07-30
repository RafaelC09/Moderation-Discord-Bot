import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='count')
    async def count(self, ctx, word: str):
        size = len(word)
        await ctx.send(f'The word "{word}" has {size} letters.')
    
    @commands.command(name='chnick')
    @commands.has_permissions(manage_nicknames=True)
    async def chnick(self, ctx, member: discord.Member, *, new_nick):
        try:
            await member.edit(nick=new_nick)
            await ctx.send(f"{member.mention}s Nickname was changed for `{new_nick}`.")
        except discord.Forbidden:
            await ctx.send("❌ I dont have permission to change this member nickname")
        except Exception as e:
            await ctx.send(f"⚠️ It happened an error: {e}")
    
    @commands.command()
    async def helpcmd(self, ctx):
        embed = discord.Embed(
            title="Help Embed",
            description="Moderation BOT\nCommands:\n!count -> Counts the letters in a word\n!chnick @member *Nickname -> Changes an member nickname\nAdmins Commands:\n!clean *number -> Cleans a number of messages from a channel\n!ban @member *reason -> Bans a member, an reason can be added\n!unban *user -> Unbans a user banned\n!kick @member *reason -> Kicks a member, an reason can be added\n!warn @member *message -> Warns a member with a message on DM",
            color=0xFF5733
        )
        embed.set_author(name="Simple BOT", url=None)
        embed.set_footer(text="This bot is only an example used for learning some notions of programming.")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, amount: int):
        if amount < 1:
            await ctx.send("Please, put a number higher than 0.")
            return
        deleted = await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{len(deleted)-1} messages cleaned!", delete_after=5)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member} was banned from server. Reason: {reason if reason else 'No reason provided.'}")
        except Exception as e:
            await ctx.send(f"I couldnt ban the user: {e}")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, user: str):
        banned_users = [entry async for entry in ctx.guild.bans()]
        nome, discriminator = user.split('#')
    
        for ban_entry in banned_users:
            user_banned = ban_entry.user
        
            if user_banned.name == nome and user_banned.discriminator == discriminator:
                await ctx.guild.unban(user_banned)
                await ctx.send(f"✅ {user_banned} was unbanned with success.")
                return
        
        await ctx.send("❌ User not found in bans list.")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member} was kicked from server. Reason: {reason if reason else 'No reason provided.'}")
        except Exception as e:
            await ctx.send(f"I couldnt kick the user: {e}")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, message):
        try:
            await member.send(f"**Aviso do servidor {ctx.guild.name}:**\n{message}")
            await ctx.send(f"Mensagem de aviso enviada para {member.mention}!")
        except discord.Forbidden:
            await ctx.send(f"Não consegui enviar mensagem privada para {member.mention}")
        except Exception as e:
            await ctx.send(f"Erro ao enviar mensagem: {e}")
        
        
    
    # @commands.command()
    # async def entra(self, ctx):
    #    if ctx.author.voice:
    #        canal = ctx.author.voice.channel
    #        voice_client = await canal.connect()
    #        await ctx.guild.change_voice_state(channel=canal, self_mute=True, self_deaf=True)
    #        await ctx.send(f'Entrei no canal {canal.name}.')
    #    else:
    #        await ctx.send("Não estás em canal de voz nenhum.")


    #@commands.command()
    #async def sai(self, ctx):
    #    voice_client = ctx.voice_client
    #    if voice_client and voice_client.is_connected():
    #        await voice_client.disconnect()
    #        await ctx.send("Saí do canal de voz!")
    #    else:
    #        await ctx.send("Não estou em nenhum canal de voz.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))