import discord
from discord.ext import commands
import stockprices 
import io

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith('!stock'):
        await message.channel.send("Invalid command. Please use the format: `!stock <ticker>`")
        return

    await client.process_commands(message)