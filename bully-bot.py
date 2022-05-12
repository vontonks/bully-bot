import discord
from discord.ext import commands
import logging
import random
import settings
import insults
import users
import gen_insult

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='$', case_insensitive=True)

@bot.command()
async def bully(ctx, *, member: discord.Member):
    #don't bully yourself
    if member == ctx.author:
        await ctx.send(random.choice(insults.self), tts=True)
        return
    
    #don't bully the bot
    elif str(member) == users.bot:
        await ctx.send(random.choice(insults.bot), tts=True)
        return
    
    #do bully peacan
    elif str(member) == "Peacan#2187":
        roll = random.randrange(1,4)
        if roll == 1:
            await ctx.send(member.mention + ' ' + random.choice(insults.peacan) + '.', tts=True)
    
    else:
        roll = random.randrange(1,5)
        if roll == 1:
            await ctx.send(member.mention + ' ' + random.choice(insults.generic) + '.', tts=True)
        
        if roll >= 2:
            await ctx.send(member.mention + ' ' + gen_insult.gen_insult(), tts=True)
        return

bot.run(settings.token)
