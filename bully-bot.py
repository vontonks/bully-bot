import discord
from discord.ext import commands
import logging
import random
import settings
import insults
import users

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='$', case_insensitive=True)

@bot.command()
async def bully(ctx, *, member: discord.Member):
    if member == ctx.author:
        await ctx.send(random.choice(insults.self))
        return
    
    elif str(member) == users.bot:
        await ctx.send(random.choice(insults.bot))
        return

    else:
        await ctx.send(member.mention + ' ' + random.choice(insults.generic) + '.')
        return

bot.run(settings.token)
