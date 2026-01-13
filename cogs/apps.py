# cogs/apps.py
import discord
from discord.ext import commands
from discord import SlashCommandGroup

class Apps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        guild_id = bot.guild_id

        # GREET
        @discord.user_command(name="Greet", guild_ids=[guild_id])
        async def greet(ctx: discord.ApplicationContext, member: discord.Member):
            await ctx.respond(f"{ctx.author.mention} says hello to the one and only, {member.mention}!")
        self.bot.add_application_command(greet)

def setup(bot):
    bot.add_cog(Apps(bot))
