import discord
import logging
import random
import re

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#give it a list of, say, 10 things
insult = ['LIST']
negative = ['LIST']
casey = ['LIST']

count = 0

@client.event

async def on_message(message):
    command = message.content
    result = re.search('<@(.*)>', command)
    if message.author == client.user:
        return
    
    print(message.content)

    if message.content.startswith('$bully <@969136945613656094>'):
        await message.channel.send(random.choice(negative))
        return

    if message.content.startswith('$bully <@261104394987110400>'):
        await message.channel.send(random.choice(casey))
        return

    if message.content.startswith('$bully'):
        print(client.user)
        user_id = result.group(1)
        await message.channel.send(f'<@{user_id}>'+ ' ' + random.choice(insult) + '.')

        


client.run('ACCESS TOKEN')
