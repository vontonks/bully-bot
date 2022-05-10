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

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# when a message arrives, do things
@client.event
async def on_message(message):

    result = re.search('<@(.*)>', message.content)
    
    if message.content.lower().startswith('$bully'):
        user_id = result.group(1)
        await message.channel.send(f'<@{user_id}>'+ ' ' + random.choice(insults.generic) + '.')

# Want to keep the ability to program specific insults for people because why not?
# maybe it can first run a check to see if the user matches a list of special users
# then rolls to decide if it givse them a specific or generic insult

# I hid my auth token like a good boy
client.run(settings.token)
