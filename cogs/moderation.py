import discord
from discord.ext import commands
#from discord.ext import clean_content

from discord.ext import commands


class Moderationcog:

    def __init__(self, bot):
        #creation of the cog, do init stuff here, also gets and stores the bot
        self.bot: commands.Bot = bot

    def __unload(self):
        #cog unloading, cleaup if needed
        pass
    
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason = "No reason given"):
     if user == ctx.bot.user:
       await ctx.send("Czemu chciałbyś mnie zbanować?")
     elif user == ctx.author:
       await ctx.send("nie możesz zbanować siebie")
     elif user.top_role > ctx.guild.me.top_role:
       await ctx.send(f':no_entry_sign: {user.name} ma role wyższą od mojej.')
     elif user.top_role > ctx.author.top_role:
       await ctx.send(f':no_entry_sign: {user.name} ma role wyższą od ciebie.')
     else:
       await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) Powód: {reason}")
       await ctx.send(f":ok_hand: {user.name} ({user.id}) został zbanowany. Powód: `{reason}`")

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(ban_members=True)
   async def forceban(self, ctx, user_id: int, *, reason = "No reason given"):
     user = await ctx.bot.get_user_info(user_id)
     if user == ctx.bot.user:
       await ctx.send("Czemu chcesz mnie zbanować?")
     elif user == ctx.author:
       await ctx.send("nie możesz zbanować siebie")
     else:
       await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) Powód: {reason}")
       await ctx.send(f":ok_hand: {user.name} ({user.id}) został zbanowany. Powód: `{reason}`.")

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(ban_members=True)
   async def softban(self, ctx, member: discord.Member, *, reason = "No reason given"):
     if member == ctx.bot.user:
       await ctx.send("Nie możesz softbanować mnie")
       return
     elif member == ctx.author:
       await ctx.send("nie możesz softbanować siebie.")
       return
     await ctx.guild.ban(member, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) Powód: {reason}")
     await ctx.guild.unban(member)
     await ctx.send(f":ok_hand: {member.name} ({member.id}) was soft-banned. Powód: `{reason}`.")

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(kick_members=True)
   async def kick(self, ctx, user: discord.Member, *, reason = "No reason given."):
     if user == ctx.bot.user:
       await ctx.send("czemu chcesz mnie wyrzucić?")
     elif user == ctx.author:
       await ctx.send("Nie możesz wyrzucić samego siebie!")
     elif user.top_role > ctx.guild.me.top_role:
       await ctx.send(f':no_entry_sign: {user.name} ma role wyższą odemnie..')
     elif user.top_role > ctx.author.top_role:
       await ctx.send(f':no_entry_sign: {user.name} ma rolę wyższą od ciebie.')
     else:
       await ctx.guild.kick(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) Powód: {reason}")
       await ctx.send(f":ok_hand: {user.name} ({user.id}) został wurzucony. Powód: `{reason}`")

    
    
def setup(bot):
    bot.add_cog(Moderationcog(bot))