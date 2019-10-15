#bot.py

import discord
import time
import asyncio


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    curse_words = ['fuck', 'Fuck', 'Shit', 'shit', 'Bitch', 'bitch', 'Trump', 'trump', 'MAGA', 'Ass', 'ass']
    if any(x in message.content.lower() for x in curse_words):
        print(f'Curse Found')
        await message.delete()
        await message.channel.send(f"{message.author.mention}, don't use such vocabulary here!")
                                   
client.run(token)
