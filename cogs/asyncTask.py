import discord
import asyncio
from discord.ext import tasks, commands

class backgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity = discord.Game("backstabbing randos"))
        print("Is Online")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

async def setup(bot):
    await bot.add_cog(backgroundTasks(bot))