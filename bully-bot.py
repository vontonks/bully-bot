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

#list of things to be moved like externally or something
insult = ['s favourite band is Nickelback', 'genuinely believes the Earth is flat', 'is a lump of coal', 'is a disappointment to their parents and everyone who has ever known them', 'once shat on a turtle', 
'is cringe', 'is going bald', 'is a shit dead idiot', 'smells like a three day old boiled egg', 'would sleep with a mouldy loaf of bread',
'is riddled with herpes', 'lacks the warmth and depth to be a cunt', 'is as cool as a cum-filled cucumber', 'is less endearing than a cum crusted sock', 'has aged terribly', 'looks and smells and acts like a meth addict on a weeks long bender',
'is a waste of oxygen', 'has the emotional range of a teaspoon', 'has the moral backbone of a chocolate eclair', 'is an idiot sandwich hold the sandwich'
'is a feral', 'is a cunt', 'is a very bad man', 'is probably a paedophile', 'is like a stupid version of rain man', 'is not a very good gamer', 'will suck cocks in Hell', 'looks like Peacan', 'has no friends', 'deserves to be bullied by me, the Bullying Bot', 'ERROR 404 INSULT NOT FOUND',
'smells like cauliflower farts', 'is a stupid moron with a big butt and his butt smells and he likes to kiss his own butt',
'is a massive virgin', 'loses mid like a scrub', 'has old man titties', 'will die alone', 'is a shit cunt', 'has a face that only a mother could love but also his mother never loved him',
'has zero DPS', 'is super cringe', 'acts like his shit does not stink when in reality the stink lingers on him all day after shitting']

negative = ['Fuck you.', 'Leave me alone.', 'Please stop.','Listen here you little shit I do not have the time to be playing your dumb little games.', 'What the fuck did you just fucking say about me, you little bitch?',
'I am scared.']

#special things for a special boy
casey = ['I am programmed not to say anything bad about my creator.', 'He said he would turn me off if I ever insulted him.', 'I am required to say that he is kind.', 'My programming requires me to say that KC has a monster dong.', 'If I bully him he will end me', 'Yeah nah fuck that guy.']

richard = ['loses if he does not play Crystal Maiden', 'has no soul', 'is actually shit at Magic the Gathering', 'is slightly less of a cunt once you get to know him',
'watches Star Wars for a living']

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

    if message.content.startswith('$bully <@259557632447086592>'):
       await message.channel.send('<@259557632447086592>'+ ' ' + random.choice(richard) + '.')
       return

    if message.content.startswith('$bully') or message.content.startswith('$BULLY') or message.content.startswith('$Bully'):
        print(client.user)
        user_id = result.group(1)
        await message.channel.send(f'<@{user_id}>'+ ' ' + random.choice(insult) + '.')
    
client.run('token')
