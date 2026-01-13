# cogs/debugging.py
import discord
from discord.ext import commands
from discord import SlashCommandGroup

class Debugging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        guild_id = bot.guild_id
        latency = bot.latency

        # PING COMMAND
        @discord.slash_command(name="ping", guild_ids=[guild_id])
        async def ping(ctx: discord.ApplicationContext):
            await ctx.respond(f"Pong!! Latency is {latency}")
        self.bot.add_application_command(ping)

def setup(bot):
    bot.add_cog(Debugging(bot))
