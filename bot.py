import asyncio
import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks, commands
import random
import backstab
import cogs.asyncTask

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = '''A bot that is a total hot mess of silicon.'''
bot = commands.Bot(command_prefix='`', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.add_cog(cogs.asyncTask.backgroundTasks(bot))
         
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format. add more dice using : to """
    totalDice = dice.split(":")
    diceResults = ""
    for i in range(len(totalDice)):
        try:
            rolls, limit = map(int, totalDice[int(i)].split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN or NdN:NdN!')
            return
        
        diceResults += str(totalDice[int(i)]) + ": " + ', '.join(str(random.randint(1, limit)) for r in range(rolls)) + " "
    await ctx.send(diceResults)

@bot.command()
async def multiargtest(ctx, *args):
    """Testing to see how many args are being seen"""
    arguments = args.split(" : ") #', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command()
async def image(ctx, args: str):
    """Grabs the map from backstab and saves it to the computer while also posting it to the discord channel"""
    arguments = args.split(" : ")
    url, name, webElement = arguments[0],arguments[1],arguments[2] 
    backstab.grabImage(url, name, webElement)
    await ctx.send(file=discord.File("C:/Users/alexz/Documents/AAA_PROXY/Programs/DisasterBot/Backstab/" + str(name) +".png"))

bot.run(str(TOKEN))
