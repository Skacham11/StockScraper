import discord
from discord.ext import commands
import stockprices 
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define your Discord bot token
TOKEN = os.getenv('DISCORD_TOKEN')

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

@client.command(name='stock')
async def stock(ctx, ticker: str):
    try:
        html = stockprices.fetch_stock_data(ticker)

        if html:
            data = stockprices.parse_stock_data(html)

            if data:
                embed = discord.Embed(title=f"{ticker.upper()} Stock Information", color=0x1E90FF)
                for key, value in data.items():
                    embed.add_field(name=key, value=value, inline=False)
                await ctx.send(embed=embed)
                buffer = io.BytesIO()
                stockprices.plot_stock_history(ticker, buffer)
                buffer.seek(0)
                await ctx.send(file=discord.File(buffer, filename=f'{ticker}_stock_plot.png'))
            else:
                await ctx.send(f"Failed to parse data for {ticker}.")
        else:
            await ctx.send(f"Failed to fetch data for {ticker}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

client.run(TOKEN)
