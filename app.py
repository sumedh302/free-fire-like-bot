import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
import threading

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Flask app for status endpoint
app = Flask(__name__)

@app.route('/')
def status():
    return jsonify({
        'status': 'active',
        'bot_name': 'Free Fire Like Bot',
        'guilds': len(bot.guilds) if bot.is_ready() else 0
    })

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')
    
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

# Load cogs
async def load_cogs():
    await bot.load_extension('cogs.likeCommands')

def run_flask():
    app.run(host='0.0.0.0', port=10000, debug=False)

async def main():
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Load cogs
    await load_cogs()
    
    # Start the bot
    await bot.start(os.getenv('TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())
