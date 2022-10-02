import nextcord
from nextcord.ext import commands, tasks

import json
import os
import re
import random

if os.path.exists(os.getcwd() + "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!", "noPing": [], "bannedWords": []}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

prefix = ["!"]
bannedWords = ["bitch","fuck","fuckkk","cock","testicles","lmfao","orgasm","fuck!!!","triggerjxl12-7777","nigga","niga","nigger","niger","fucker","motherfucker","fucka","asshole","pussy","cum","anal","fucking","bitching","bitchy","semen"]


bot = commands.Bot(command_prefix=prefix)

@bot.slash_command()
async def loadcog(ctx, cog):
    bot.load_extension(f"cogs.{cog}")

@bot.slash_command()
async def unloadcog(ctx, cog):
    bot.unload_extension(f"cogs.{cog}")

@bot.slash_command()
@commands.has_permissions(administrator=True)
async def addbannedword(ctx, word):
    if word.lower() in bannedWords:
        await interaction.response.send_message("Already banned")
    else:
        bannedWords.append(word.lower())

        with open("./config.json", "r+") as f:
            data = json.load(f)
            data["bannedWords"] = bannedWords
            f.seek(0)
            f.write(json.dumps(data))
            f.truncate()

        await ctx.message.delete()
        await interaction.response.send_message("Word added to banned words.")

@bot.slash_command()
@commands.has_permissions(administrator=False)
async def removebannedword(ctx, word):
    if word.lower() in bannedWords:
        bannedWords.remove(word.lower())

        with open("./config.json", "r+") as f:
            data = json.load(f)
            data["bannedWords"] = bannedWords
            f.seek(0)
            f.write(json.dumps(data))
            f.truncate()

        await ctx.message.delete()
        await interaction.response.send_message("Word remove from banned words.")
    else:
        await interaction.response.send_message("Word isn't banned.")

def msg_contains_word(msg, word):
    return re.search(fr'\b({word})\b', msg) is not None

@bot.event
async def on_message(message):
    messageAuthor = message.author
    dontswear = [f"{messageAuthor.mention} Please do not swear this is a sfw server",f"{messageAuthor.mention} Be nice please",f"{messageAuthor.mention} Heres some soap to clean that dirty mouth of yours🧼",f"{messageAuthor.mention} Say that again and imma whoop your keister",f"{messageAuthor.mention} Dude chill, just chill",f"{messageAuthor.mention} Get your head out of the gutter please",f"{messageAuthor.mention} Yeah sorry, no",f"{messageAuthor.mention} honey please!"]

    if bannedWords != None and (isinstance(message.channel, nextcord.channel.DMChannel) == False):
        for bannedWord in bannedWords:
            if msg_contains_word(message.content.lower(), bannedWord):
                await message.delete()
                await message.channel.send(random.choice(dontswear))

    await bot.process_commands(message)

bot.run("ODAwNjA0MjgwNzU0Mjc0MzA2.YAUi1w.V2ASmWkKVZckMYdeYxWrf4DN_4M")
