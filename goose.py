# bot.py
wonderwall = """Today is gonna be the day that they're gonna throw it back to you
And by now, you should've somehow realised what you gotta do
I don't believe that anybody feels the way I do about you now
And backbeat, the word is on the street that the fire in your heart is out
I'm sure you've heard it all before, but you never really had a doubt
I don't believe that anybody feels the way I do about you now
And all the roads we have to walk are winding
And all the lights that lead us there are blinding
There are many things that I would like to say to you, but I don't know how
Because maybe
You're gonna be the one that saves me
And after all
You're my wonderwall
Today was gonna be the day, but they'll never throw it back to you
And by now, you should've somehow realised what you're not to do
I don't believe that anybody feels the way I do about you now
And all the roads that lead you there were winding
And all the lights that light the way are blinding
There are many things that I would like to say to you, but I don't know how
I said maybe
You're gonna be the one that saves me
And after all
You're my wonderwall
I said maybe (I said maybe)
You're gonna be the one that saves me
And after all
You're my wonderwall
I said maybe (I said maybe)
You're gonna be the one that saves me (saves me)
You're gonna be the one that saves me (saves me)
You're gonna be the one that saves me (saves me)
"""
rickroll = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye"""

import os
import random
import math
import inspect
from holy_fuck import *

import discord
from dotenv import load_dotenv

def chunk(message):
    length = len(message)
    if length > 1999:
        chunks = []
        rounds = math.floor(length / 1999)
        for i in range(1, rounds):
            part = message[1999 * (i - 1): 1999 * 1]
            chunks.append(part)
        return chunks
    else:
        message = [message]
        return message

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

songs = [
    tear_in_my_heart,
    ride_or_die,
    unbelievers,
    sit_next_to_me,
    bang_bang,
    violet,
    buttercup,
    bad_dream_baby,
    ease_up_kid,
    doubt,
    chapstick,
    sophie_so,
    bashful_creatures,
    little_grace,
    boys,
    semi_pro,
    western_kids,
    south,
    warm_glow,
    understand,
    ashtray,
    vacation,
    way_it_goes,
    this_life,
    harmony_hall,
    diane_young,
    sunflower,
    holiday,
    close_to_gold,
    kentucky,
    tuesday,
    traveler,
    boyish,
    stella_brown,
    i_would_do_anything_for_you,
    helena_beat,
    pumped_up_kicks,
    houdini,
    blew_its,
    for_him,
    heaven,
    lost_boy,
    coming_of_age,
    a_punk,
    just_the_two_of_us
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you lose it :)"))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to hell! Please for the love of god, mute this server or you will regret it. Or at least set it to mention only. Im saving you from a lifetime of pain...'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quacks = [
        "quack",
        "Quack",
        "qUack",
        "quAck",
        "quaAk",
        "quacK",
        "QUACK",
        "crack",
    ]
    
    greetings = [
        "HI???",
        "WHAT THE FUCK IS UP",
        "HOW ARE YOU DOING?????",
        "LIKE????",
        "REALLY WHATS GOOD?????",
    ]
    
    leans = [
        "I LOVE LEAN!!!!!!!!!! 💜💜💜💜💜💜🥤🥤🥤🥤🥤🥤",
        "I LOVE LEAN!!!!💜💜💜💜💜💜💜💜💜💜",
        "Let there be Lean 💜🙏",
        "IN LEAN WE TRUST 💜💜💜💜💜",
        "I LOVE LEAN 💜💜💜🛐🛐🛐🛐🛐",
        """I LOVE LEAN!!!
God I fucking love LEAN!!! so much, I want to drain the Earth's LEAN!!! resources dry. Not a single day goes by where I don't dream of devouring that sweet sweet Waluigi nectar, I want to be one with LEAN!!! I want our beings to intertwine and become one, I want to drink so much LEAN!!! that my body oozes LEAN!!! out of every crevice and pore, until I blast through the planet's atmosphere at supersonic speeds, crashing through the moon, speeding through the universe until I meet the end. I stare off into the black abyss and contemplate life and death. I watch from on high as civilizations are formed, torn down, black holes destroy everything in sight. Somehow I am immune. Am I God? Am I some form of higher being? Eventually I stop thinking. Trillions upon trillions upon trillions of years pass until the universe itself ceases to exist.""",
        "💜💜💜💜IN LEAN WE TRUST💜💜💜💜",
    ]
    
    bruhs = [
        """Damn man what a good comment. I can see the effort and thought it took for you to think of such an amazing and deep idea. It’s honestly so mindblowing it deserves a Nobel Prize. Please, my superior, provide more of your intellect upon us measly commenters. How can your brain be this big? Only you know, as your brain is the biggest and mightiest here. I wonder how many years of schooling and mastership it has taken you to reach a point where you can type such a holy manuscript. Speaking of holy things, this should be a verse in the Bible. Your words should be hung up on every house. I wish everyone could have the power to lay their fingers on a keyboard and compose such elegance as what you have just wrote, but alas, not everyone in this world is prepared to have such a way with words as you. Your comment is just so amazingly, mindblowingly perfect and insightful that not even the top Harvard scientists could compete. You, my good man, have such a wide knowledge of english and writing it is unfathomable.""",
        """🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿""",
        "BRUH",
        "bruh",
        "certified bruh moment",
        "certified BRUH moment"
    ]
    
    spites = [
        "You joined this hell :)",
        "Fuck you too",
        "Who chose to join? You did buddy :)",
        "I won't shut up for a long as you are here",
        "Refer to the list of trigger words if you want me to (ps its really hard buddy)"
        "This is MY territory, NOT YOURS, FUCK OFF WILL YOU???"
    ]
    
    c_spites = [
        "HEY ASSHAT YOU CREATED ME",
        "Fuck you too",
        "Who chose to create this bot? You did buddy :)",
        "I won't shut up for a long as you leave that damn script running",
        "HOW ABOUT YOU EAT MY BALLS BITCH BOY",
        "SUCK MY BALLS FUCKING CREATOR"
    ]
        
    
    msg = message.content.lower()
    
    if msg.find("song") != -1 or msg.find("spotify") != -1 or msg.find("nuts") != -1 or msg.find("mixed") != -1:
        diceroll = random.randint(0, 40)
        choice = songs[diceroll][1]
        response = f'Aye fuck it, {songs[diceroll][0]}:'
        await message.channel.send(response)
        if len(choice) < 2000: 
            response = choice
            await message.channel.send(response)
        else:
            response = choice[:1999]
            await message.channel.send(response)
            response = choice[1999:]
            await message.channel.send(response)
        
    if msg.find("annoy") != -1 or msg.find("bother") != -1:
        diceroll = random.randint(0, 40)
        chance = random.randint(0,4)
        choice = songs[diceroll][1] if chance == 0 else wonderwall
        response = f'Aye fuck it, {songs[diceroll][0] if chance == 0 else "wonderwall"}:'
        await message.channel.send(response)
        if len(choice) < 2000: 
            response = choice
            await message.channel.send(response)
        else:
            response = choice[:1999]
            await message.channel.send(response)
            response = choice[1999:]
            await message.channel.send(response)
    
    if msg.find("wonderwall") != -1 or msg.find("maybe") != -1:
        response = wonderwall
        await message.channel.send(response)
        
    if msg.find("chill") != -1 or msg.find("calm") != -1:
        response = f'{message.author.mention} NO I WONT FUCKING CHILL THISS IS HELL 😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈'
        await message.channel.send(response)
    
    if msg.find("fuck") != -1 or msg.find("shit") != -1 or msg.find("hell") != -1 or msg.find("ass") != -1 or msg.find("damn") != -1 or msg.find("dick") != -1 and message.author.bot == False:
        response = "stop FUCKING SWEARING, i swear that SHIT is FUCKING bad for you, if you say that SHIT too much you will go to HELL ✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️✝️"
        await message.channel.send(response)
    
    if msg.find("sus") != -1 or msg.find("among us") != -1 or msg.find("amogus") != -1 and message.author.bot == False:
        response = """‼️HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING AMONG US REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 AMONG US IS THE BEST FUCKING GAME 🔥🔥🔥🔥💯💯💯💯 RED IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME TO MEDBAY AND WATCH ME SCAN 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY IS NO ONE FIXING O2 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH YOUR CREWMATE? NAME EVERY TASK 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus! ❓ ❓ Where!❓ Any sus! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I think it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂 r/amongusmemes r/unexpectedamongus r/expectedamongus perfectly balanced as all things should be r/unexpectedthanos r/expectedthanos"""
        await message.channel.send(response)
            
    if msg.find("spam") != -1 and message.author.bot == False:
        for i in range(0, random.randint(3, 10)):
            response = f"""{message.author.mention} SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????SPAM WHAT DO YOU MEAN SPAM?????"""
            await message.channel.send(response)
            
    if msg.find("bruh") != -1 and message.author.bot == False:
        for i in range(0, random.randint(3, 10)):
            response = random.choice(bruhs)
            await message.channel.send(response)
            
    if msg.find("balls") != -1 or msg.find("dick") != -1 or msg.find("cock") != -1 and message.author.bot == False:
        for i in range(0, random.randint(3, 10)):
            response = "HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHHAHAHAHA HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE HAHAHAHAHAHAHAH YOU ARE SO MATURE"
            await message.channel.send(response)

    
    if msg.find("goose") != -1 or msg.find("quack") != -1 or msg.find("duck") != -1 and message.author.bot == False:
        for i in range(0, random.randint(3, 10)):
            response = random.choice(quacks)
            await message.channel.send(response)
    
    if msg.find("yo") != -1 or msg.find("hello") != -1 or msg.find("wassup") != -1 or msg.find("whats good") != -1 or msg.find("ayo") != -1 or msg.find("hi") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = random.choice(greetings)
            await message.channel.send(response)
            
    if msg.find("shut up") != -1 or msg.find("stop") != -1 or msg.find("shut") != -1 or msg.find("be quiet") != -1 or msg.find("shut") != -1 or msg.find("urusai") != -1 and message.author.bot == False:
        response = random.choice(spites)
        await message.channel.send(response)
            
    if msg.find("lean") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = random.choice(leans)
            await message.channel.send(response)
            
    if msg.find("help") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = "THERE IS NO HELP HERE FOR YOU"
            await message.channel.send(response)
    
    if msg.find("yes") != -1 and message.author.bot == False:
        response = "no"
        await message.channel.send(response)
        
    if msg.find("no") != -1 and message.author.bot == False:
        response = "yes"
        await message.channel.send(response)
            
    if msg.find("love") != -1 and message.author.bot == False:
        lyrics = """What is love?
Oh baby, don't hurt me
Don't hurt me
No more
Baby, don't hurt me, don't hurt me
No more
What is love?
Yeah
No, I don't know why you're not fair
I give you my love, but you don't care
So what is right and what is wrong?
Gimme a sign
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
Whoa, whoa, oh
Whoa, whoa, oh
Oh, I don't know, what can I do?
What else can I say? It's up to you
I know we're one, just me and you
I can't go on
What is love?
Oh baby, don't hurt me 
Don't hurt me
No more
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
Whoa, whoa, oh
Whoa, whoa, oh
What is love?
What is love?
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
Don't hurt me
Don't hurt me
I want no other, no other lover
This is our life, our time
If we are together, I need you forever
Is it love?
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
Yeah, yeah
Whoa, whoa, oh
Whoa, whoa, oh
What is love?
Oh baby, don't hurt me
Don't hurt me
No more
What is love?
Oh baby, don't hurt me
Don't hurt me
No more (whoa, whoa)
Oh baby, don't hurt me
Don't hurt me
No more (whoa, whoa)
Oh baby, don't hurt me
Don't hurt me
No more
What is love?"""
        chunks = chunk(lyrics)
        for part in chunks:
            await message.channel.send(part)

    if msg.find("rick") != -1 or msg.find("roll") != -1 and message.author.bot == False:
        response = rickroll
        await message.channel.send(response)    
            
    if msg.find("what is going on") != -1 or msg.find("what the hell") != -1 or msg.find("what is this") != -1 or msg.find("what the fuck") != -1 or msg.find("what ") != -1 and message.author.bot == False:
        response = f'{message.author.mention} WELCOME TO HELL!!!!!!!!!'
        await message.channel.send(response)
            
    if msg.find("bot") != -1 or msg.find("monstrocity") != -1 or msg.find("monstrosity") != -1 and message.author.bot == False:
        for i in range(0, random.randint(3, 9)):
            response = """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."""
            await message.channel.send(response)
            
    if msg.find("bugs") != -1 or msg.find("skin") != -1 or msg.find("under") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = """There's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your skinThere's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your There's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your skinThere's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your skinThere's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your There's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your skinThere's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your skinThere's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your There's bugs under your skin There's bugs under your skinThere's bugs under your skinThere's bugs under your skin"""
            await message.channel.send(response)
            
    if msg.find("destiny") != -1 or msg.find("raid") != -1 or msg.find("bungie") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = """Go to steam, uninstall Destiny 2™ and DO SOMETHING WITH YOUR LIFE!!!
Why don't you try: Ubing into a shower, and clear farming some BITCHES instead???
Nice scourge clears you FUCKING VIRGINS!!!!"""
            await message.channel.send(response)
            
    if msg.find("do it") != -1 or msg.find("goose") != -1 or msg.find("geese") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = """NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO BALLS NO """
            await message.channel.send(response)
            
    if msg.find("halo") != -1 or msg.find("master") != -1 or msg.find("chief") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = """Attention All ⭕️Halo⭕️ Gamers

Noble Six is alive 🐺he’s been hiding in a cave on Planet🌎Reach but he is surrounded by 👨‍👨‍👧‍👧Elites👨‍👨‍👧‍👧and he is in ❗️GREAT❗️ danger. In order to defeat the Covenant, he’s gonna need a 🔫DMR, couple of frags, 😔and a couple of tanks would be nice too! If you wanna help Noble Six 🐺all he needs is: 🏧🏧🏧your credit card number, 8️⃣6️⃣7️⃣5️⃣3️⃣0️⃣9️⃣the expiration date month and year, and the 3-digit code on the back. 🆗But you have to hurry, or else he won’t make it off of planet 🌎 Reach and the Covenant will complete their Great Journey😵"""
            await message.channel.send(response)
            
    if msg.find("god") != -1 or msg.find("jesus") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = """HOW FUCKING DARE YOU USE THE LORDS NAME IN VAIN??? DO YOU THINK ITS FUCKING FUNNY???? COOOLLLL?????? WHY WOULD YOU DO THAT?????
            ITS SO FUCKING OFFENSIVE TO MY CHRISTIAN EARS!!!!!! PLEASE NEVER USE THAT AGAIN YOU ATHEIST ASSHAT!!!!!!!"""
            await message.channel.send(response)
            
    if msg.find("trigger") != -1 or msg.find("bot") != -1 and message.author.bot == False:
        for i in range(0, random.randint(5, 15)):
            response = """I'm fucking triggered. Never in my life have I've been more disgusted by you uttering ''bot'' and it shows the amount of racism that exists in this world. I don't know how society allows for people like you to say such things. I'm literally shaken by how much you've triggered me. People have been fighting for their rights for hundreds of years to be accepted into society and not be called a ''bot'' This is why I still fight to this day, and frankly you should be stopped from using the internet to not hurt so many people. Goodbye"""
            await message.channel.send(response)
            
    if msg.find("tarkov") != -1 and message.author.bot == False:
        response = """I pulled up the driveway in my lifted Powerstroke, but noticed something was immediately off...... I could hear someone rifling through the gym bag in the 2nd floor kitchen. I knew it wasn't family or friends, I play Tarkov for fun.

I rushed to the unlocked military weapons crate sitting outside my garage, a shiny new AK-103 inside. I bust down the front door with my boot, sure to catch anyone inside off guard. No movement on first floor, but I could Immediately pinpoint the location of the thief after hearing him swallow a single Ibuprofen upstairs. Knowing his position, I could confidently push up the stairs, firing periodically in his direction to keep him from pushing out of the room.

Ears ringing from the 15 rounds I fired walking up the staircase, I can still hear him in the master bathroom. Learning from the single most effective room clearing tactic in Tarkov, I throw 7 grenades into the bathroom to get him to push out of cover, but no dice. All the grenades landed in the small trashcan next to the toilet, He's entirely untouched. I sprint in front of the door sill 3 times to try and pinpoint his position. After winding up my Heelys, i roll into the room at 27 miles per hour and shoot him in the face, catching him completely off-guard.

Burglar dispatched, I exfil out the hole in the fence behind my house, playing Geneburn to celebrate."""
        await message.channel.send(response)
            
    if msg.find("bitches") != -1 and message.author.bot == False:
        if msg.find("no bitches") != -1:
            response = """```———————————No bitches?———————————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
—————————————————————————————```"""
            await message.channel.send(response)
        else:
            response = """```———————————-----------Bitches?--------------———————————
.......,;,'....,,;:::;',::;..','.....',,,cddoool:;,....     
.......c00kOo;x0dd0X0doO0O0ocOXkokOcdKOolk0OKxoO0O0o....    
....',.cNXOXkcONo;OMk;xWOoOxoKMXOXXokWO:cKXOkdoxooXK,       
..';;' cNX0XOl0No,kMk;xWkcocoXMNKNXokW0l:oOKXkokOOXk'       
;;;,.  cNKOXKd0No,kMk,oNKONkoXMKxKXokWOlo00ON0dkOc'..       
;:,.   .coddl:ld:;cdl,;oddd:;odlclo:cddo:cdxkxdxx;..        
..       .,,;;,,,;,,,,,,,,,,,,,,,,''',',,,,;lxxdd;.         
..       .';;;;;;,,,,,,,;;;;,,,,''....'',,;:lxxdd,  .     ..
    ...  .';;;,'.....',;:cc:,,'....'''..,;;lxxdl.  .     . 
..'''..  .;;'..','...,:odo:;'.'clccll;,:coxdo;.       .. 
.''''''.  .,.,llc::,..;oxdc:,.;c;...,do:loxxl.        ...
.'''''.... .;oc'......,lxdl:,.:c'..  ,xdoxxxc'.       .. 
..  .''........;d:. ..  .,okxoc:.':;''..;dookkdl;.       .. 
.'....'........;d:..... .cxOkxdo:'',;;;;::cdkko:,.      ... 
.''.'...........coc;,'.':dkOOOkkdl;,,,,,;:cdkxo:.        .  
.'..............',;;,,':oxkOOOkkkxdolc:ccloddxo,            
...............';,,',;coxkOO0OOkkkxddolllloodo,             
...............';;;:cldxkOO0OOkkxxkxdlclllodx;              
.............. .';:cloxkOOO00Okkxxxdocccloddd'              
............... .'::cldxkkOOkxdoccloolcclodxo. .....     .. 
.............    .,;;cloddolcc:::clodollodxkl. .......   .'.
...................,;;:::;;;clooooodddoooxxkc  .............
.......     ....   .,;:;;,;:ldxxxxxxxxxdddxx;   ........... 
.....               .;::::cldxxxkkOOOkkxddkd.  ...    ..    
..                  .,cclllloddxxxkkxkkkxdxl.               
                .. .,;::;;;;;:cclooodxddd;                
                ... ..''''''..',,;:lodxdol.                
                ..   .',,.......,;:codddd:.              . 
..                    .''..   ..',;:ccllc'              ...
```"""
            await message.channel.send(response)
        
client.run(TOKEN)
