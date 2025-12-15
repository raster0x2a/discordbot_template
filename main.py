import os

import discord


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready(): 
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.content == "!ping":
        await message.channel.send("pong")

if __name__ == "__main__":
    token = os.environ['DISCORD_BOT_TOKEN']
    client.run(token)
