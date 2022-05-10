import discord
import logging
import random
import re
import settings
import insults

#logger because reasons I guess
logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)

client = discord.Client()

#kindly let me know the bot is logged in
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    command = message.content
    result = re.search('<@(.*)>', command)
    
# make it so the bot doesn't talk to itself -- maybe not necessary since it responds to the $bully command?
    if message.author == client.user:
        return

# this is so I can see what it's up to but I'm sure the logger should be doing that
    print(message.content)

# dunno how to clean this mess up. 
# Want to keep the ability to program specific insults for people because why not?
# maybe it can first run a check to see if the user matches a list of special users
# then rolls to give them a specific or generic insult

    if message.content.startswith('$bully <@969136945613656094>'):
        await message.channel.send(random.choice(insults.negative))
        return

    if message.content.startswith('$bully <@261104394987110400>'):
        await message.channel.send(random.choice(insults.casey))
        return

    if message.content.startswith('$bully <@259557632447086592>'):
       await message.channel.send('<@259557632447086592>'+ ' ' + random.choice(insults.richard) + '.')
       return

    if message.content.startswith('$bully') or message.content.startswith('$BULLY') or message.content.startswith('$Bully'):
        print(client.user)
        user_id = result.group(1)
        await message.channel.send(f'<@{user_id}>'+ ' ' + random.choice(insults.generic) + '.')

# I hid my auth token like a good boy
client.run(settings.token)