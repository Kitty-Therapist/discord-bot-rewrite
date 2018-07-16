import random
import time
from datetime import datetime

import discord
from discord.ext import commands
from discord.ext.commands import clean_content

class Basecog:

             def __init__(self, bot):
                 #creation of the cog, do init stuff here, also gets and stores the bot
                 self.bot: commands.Bot = bot
                     
                     
             def __unload(self):
                 #cog unloading, cleaup if needed
                 pass
    
    
             @commands.command()
             async def ping(self, ctx:commands.Context):
                 if await self.bot.is_owner(ctx.author):
                     t1 = time.perf_counter()
                     await ctx.trigger_typing()
                     t2 = time.perf_counter()
                     await ctx.send(f":hourglass: ping do Bramy (Gateway) {round((t2 - t1) * 1000)}ms :hourglass:")
                 else:
                     await ctx.send(":ping_pong:")

             @commands.command()
             async def info(*args):
                 await ctx.send("wersja biblioteki discord.py to:" + discord.__version__)

             @commands.command()
             async def shutdown(*args):
                 await ctx.send("shutting down")
                 await sys.exit(0)
             
             @commands.command()
             async def say(self, content):
                 await self.bot.say(content)
    
    
def setup(bot):
    bot.add_cog(Basecog(bot))


