# cogs/greetings.py
import discord
from discord.ext import commands
from discord import SlashCommandGroup

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        guild_id = bot.guild_id

        # HELLO COMMAND
        @discord.slash_command(name="hello", guild_ids=[guild_id])
        async def hello(ctx: discord.ApplicationContext):
            await ctx.respond("Hello there! 😊")
        self.bot.add_application_command(hello)

        # GOODBYE COMMAND
        @discord.slash_command(name="goodbye", guild_ids=[guild_id])
        async def goodbye(ctx: discord.ApplicationContext):
            await ctx.respond("See ya later! 🫡")
        self.bot.add_application_command(goodbye)

def setup(bot):
    bot.add_cog(Greetings(bot))
