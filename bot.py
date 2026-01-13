import os
import discord
from dotenv import load_dotenv

TESTING = True

load_dotenv()

if TESTING:
    TOKEN = os.getenv('TEST_TOKEN')
    GUILD_NAME = os.getenv('TEST_GUILD')
    GUILD_ID = os.getenv('TEST_ID')
else:
    TOKEN = os.getenv('SEXYBOT_TOKEN')
    GUILD_NAME = os.getenv('SEXYBOT_GUILD')
    GUILD_ID = os.getenv('SEXYBOT_ID')

# Set intents
intents = discord.Intents.default()
intents.members = True  # required for on_member_join

bot = discord.Bot(intents=intents)
bot.guild_id = GUILD_ID # Let's Cogs access the guild ID

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

cogs_list = [
    'greetings',
    'debugging',
    'apps',
]
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(TOKEN) # run the bot with the token