import discord
import asyncio
from discord.ext import tasks, commands

class backgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.messages_to_delete = {}
        
#    def cog_unload(self):
#        self.printer.cancel()

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        if message.author == self.bot.user:
            return  # Ignore messages from the bot itself

        # If in the right channel
        #TODO put this as a env var or something
        if message.channel.id == 1177040225827029143:
            await message.channel.send("Heart")
            await self.schedule_message_deletion(message, 1)
            #Should also make that var or something

    async def schedule_message_deletion(self, message, delay_minutes):
        await message.delete(delay=delay_minutes * 60)  # Convert minutes to seconds
        self.messages_to_delete[message.id] = asyncio.get_event_loop().time() + (delay_minutes * 60)

        # Clean up the dictionary after the message is deleted
        await asyncio.sleep(delay_minutes * 60)
        del self.messages_to_delete[message.id]

    async def check_scheduled_deletions(self):
        while True:
            current_time = asyncio.get_event_loop().time()
            messages_to_delete_copy = self.messages_to_delete.copy()

            for message_id, scheduled_time in messages_to_delete_copy.items():
                if current_time >= scheduled_time:
                    message = self.bot.get_channel(message.channel.id).get_partial_message(message_id)
                    if message:
                        await message.delete()
                    del self.messages_to_delete[message_id]

            await asyncio.sleep(10)  # Adjust the sleep interval as needed


    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

        #1177040225827029143