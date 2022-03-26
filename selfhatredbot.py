#import all needed packages
from http import client
import discord
import discordapi
import os

client = discord.Client()

#define the token
token = os.environ['TOKEN']

# When the bot is ready, print to chat
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# When a message is sent in the chat
@client.event
async def on_message(message):
    # If the message is from the bot, ignore it
    if message.author == client.user:
        return

    else:
        # make the message lowercase
        message.content = message.content.lower()

        # the bot will only respond to messages that start with the prefix / or !
        if message.content.startswith('/' or '!'):
            # if the message is a ping, respond with pong
            if message.content.startswith('/ping'):
                await client.send_message(message.channel, 'pong')
            
            # if the message is hey, hello or hi, respond with "hey fuck you"
            elif message.content.startswith('/hey' or '!hey' or '/hello' or '!hello' or '/hi' or '!hi'):
                await client.send_message(message.channel, 'hey fuck you')

            # if the message is a question, respond with "Shouldn't you know nerd"
            elif message.content.startswith('/question' or '!question'):
                await client.send_message(message.channel, 'Shouldn\'t you know nerd')

            # if the message is a joke, respond with "You're not funny stop trying"
            elif message.content.startswith('/joke' or '!joke'):
                await client.send_message(message.channel, 'You\'re not funny stop trying')