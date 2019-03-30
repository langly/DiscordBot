        
import discord
import settings
from lametric import * 


settings.init("bot.conf")

## Your LaMetric IP and token goes here
l = LaMetric(settings.get('lametric_ip'), settings.get('lametric_key'))
l.notify(2867, "paa")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    print(message.content)
    l.notify(2867, message.content)

@client.event
async def on_member_update(old, new):
    if ( old.game == None and new.game != None):
        ## We can now assume that we have started playing a game.
        s = "%s started playing %s" % (new.name, new.game)
        print(s)
        l.notify(2867,s)



@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)
    print("---------")

client.run(settings.get('discord_key'))
