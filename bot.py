import discord
from discord.ext import commands
import stockprices 
import io

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)