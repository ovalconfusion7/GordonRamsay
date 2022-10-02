import random
import nextcord
import os
from nextcord import Interaction
from nextcord import client
from nextcord.enums import ContentFilter
from nextcord import member
import config


from nextcord.ext import commands

import giphy_client
from giphy_client.rest import ApiException



bot = commands.Bot(command_prefix=config.PREFIX)


testServerId = 946065301563396127

weekly_jokes = ["Some cause happiness wherever they go, others whenever they go","I can’t believe I got fired from the calendar factory. All I did was take a day off","I spent the last 2 years looking for my ex girlfriend's killer...... ||no one will do it||"
,"There are immigrants who came to your country that stole jobs and murdered the local population, we call those immigrants the founding fathers","I went to a party one day and Brad Pitt was there, they say never meet your heroes but i think Brad handled it really well","I was involved in a one night stand that went horribly wrong, we've been married 3 years now","My therapist says I'm addicted to revenge. We’ll see about that","Most people are shocked when they find out i'm not a good elctrician","Never judge someone till you walk a mile in their shoes, that way when you do judge them you'll be a mile away and have their shoes","The man who invented Velcro has died. RIP.","I have a few jokes about unemployed people, but none of them work."]

@bot.event
async def on_ready():
  activity = nextcord.Game(name="I̳̿͟͞d̳̿͟͞i̳̿͟͞o̳̿͟͞t̳̿͟͞ ̳̿͟͞B̳̿͟͞a̳̿͟͞g̳̿͟͞u̳̿͟͞e̳̿͟͞t̳̿͟͞t̳̿͟͞e̳̿͟͞", type=3)
  await bot.change_presence(status=nextcord.Status.online,activity=activity)

@bot.slash_command(name='burger')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("🍔 Here you go enjoy!")

@bot.slash_command(name='fishnchips')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("What in broken teabags is that!< who pairs fish with chips!, go back to britain please")

@bot.slash_command(name='potato')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Do i look like a ||words reserved for the real Gordon|| farmers market to you")

@bot.slash_command(name='chicken')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Ask for kfc pls just chicken isn't specific enough")

@bot.slash_command(name='fish')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Wait! wait! what type is it fried, smoked baked? make up ur mind and then talk to me")

@bot.slash_command(name='wine')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Sorry, i don't serve alcoholics")

@bot.slash_command(name='weed')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Woah, woah! lets not go there buddy")

@bot.slash_command(name='kfc')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("🍗🍗 Here you go a plateful of kentuck fried crap!")

@bot.slash_command(name='icecream')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("OK! :ice_cream: You want sprinkles with that?")

@bot.slash_command(name='pizza')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Hope you life pinnaples! 🍕")

@bot.slash_command(name='chocalate')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Here you go 🍫 straight from an overpirced duty free that imports stuff from belgium")

@bot.slash_command(name='milo')
async def versiuon(interaction: Interaction):
    await interaction.response.send_message(" Ok :coffee: Lemme guess you a cricket fan?")

@bot.slash_command(name='brownie')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Please try soaking this in vanilla ice cream :chestnut:")

@bot.slash_command(name='fries')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("The cause for your heartace is here! 🍟")

@bot.slash_command(name='kottu')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Takata Takata Tak Tak Tak :curry:")

@bot.slash_command(name='boba')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Drink it slowly ok? i don't have time for refills :bubble_tea:")

@bot.slash_command(name='pudding')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Woah, woah! i can't just give you pudding what type is it figi? or other puddings of which the name i have definetely not forgoten")

@bot.slash_command(name='vivs')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Sorry i'm not allowed to server garbage to people")

@bot.slash_command(name='shen')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("One simp coming up")

@bot.slash_command(name='ima')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Sorry i don't have that, but u can find it in the mental facility")

@bot.slash_command(name='nehan')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Umm try looking in the toilet or maybe sewer")

@bot.slash_command(name='tea')
async def gordon(interaction: Interaction):
    await interaction.response.send_message(":tea: One lump or two?")

@bot.slash_command(name='burrito')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("I got you covered fam 🌯 ")

@bot.slash_command(name='subway')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Call it sooubway dude https://tenor.com/view/we-dont-do-that-here-black-panther-tchalla-bruce-gif-16558003")

@bot.slash_command(name='coffee')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Burnin that mid night oil? :coffee:")

@bot.slash_command(name='yes')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Ok here you go then :sparkles:")

@bot.slash_command(name='no')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Ok but it's gonna test pretty bland though 🙄")

@bot.slash_command(name='taco')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("¡Aquí tienes, disfruta! 🌮")

@bot.slash_command(name='cake')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Hope theres a gym near ur place no one can resist my grandmas recipe 🍰")

@bot.slash_command(name='pancake')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Alright then who gets the milkshake oh btw u want honey with that 🍯")

@bot.slash_command(name='milkshake')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Oh so it was u! 🥤")

@bot.slash_command(name='cola')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Yeah don't that have that got moo pop though :champagne: ")

@bot.slash_command(name='lollipop')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Your dentist is gonna be rich well.. richer 🍭")

@bot.slash_command(name='biriyani')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Straight from nehan's kitchen :curry:")

@bot.slash_command(name='imeth')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("There are somethings that are too good for people to have :pensive:")

@bot.slash_command(name='cookie')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Right out of the emoji bar just for you :cookie:")

@bot.slash_command(name='hello')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Hello, im gordon ramsay without the swearing what can i do for you")

@bot.slash_command(name='1')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("https://tenor.com/view/minion-bonk-hammer-minions-despicable-me-gif-5290684")

@bot.slash_command(name='2')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("https://tenor.com/view/hit-baseball-bat-hit-head-gif-14011790")

@bot.slash_command(name='hey')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Hai!")

@bot.slash_command(name='lasagna')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Share some with Oddie :bricks: i'm seriously running out of emotes")

@bot.slash_command(name='donut')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("-INSERT COP JOKE HERE- 🍩")

@bot.slash_command(name='pasta')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("I can't think of anything italian to say so here 🍝")

@bot.slash_command(name='hotdog')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Here 🌭 if you eat enough of these you can make the term sausage fest sfw ||fyi im kidding||")

@bot.slash_command(name='salad')
async def gordon(interaction: Interaction):
    await interaction.response.send_message(" 🥗 So what made you change your mind?, what it the mirror or the heartburn ||or the fact that your jewish||")

@bot.slash_command(name='salmon')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Getting fancy now are we? 🐟, seriously i have to ask are you trying to hunt bears or something?")

@bot.slash_command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    await interaction.response.send_message(f'{member} Was bonked out of this server.')

@bot.slash_command(name='ban')
@commands.has_permissions(kick_members=True)
async def ban(ctx, member : nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    ban_messages = ['bye' f"{member} miss u never!", 'Have funn!' f"{member}",  f"{member} i never really like u anyway", "see u later"f"{member}"]
    await ctx.message.channel.send(random.choice(ban_messages))

@bot.slash_command(name='scallops')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("I have no idea what scallops look like so here is the fanciest looking thing windows + dot gave me 🍲")

@bot.slash_command(name="ping")
async def gordon(interaction: Interaction):
    await interaction.response.send_message(f'Ping: {round(bot.latency * 1000)}ms')

@bot.slash_command(name='help2')
async def gordon(interaction: Interaction):
    await interaction.response.send_message("Ask for any food item with a ! in front of it, Gordons got it for you | say !joke for well.. a joke")

user = nextcord.member

@bot.slash_command
async def cat(context,*,q='cat cute'):
    api_key = 'SbnWbiNtkNyvcOCLyRAIEqzH45O6p8Fv'
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key,q,limit=100,rating='g')
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = nextcord.Embed(tittle="with pleasure")
        emb.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await context.channel.send(embed=emb)

    except ApiException as e:
        print ("Exception when calling Api")

@bot.slash_command(name='dog')
async def gordon(context,*,q='doggo '):
    api_key = 'SbnWbiNtkNyvcOCLyRAIEqzH45O6p8Fv'
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key,q,limit=100,rating='g')
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = nextcord.Embed(tittle="with pleasure")
        emb.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await context.channel.send(embed=emb)

    except ApiException as e:
        print ("Exception when calling Api")

@bot.slash_command(name='gordon')
async def gordon(context,*,q=''):
    api_key = 'SbnWbiNtkNyvcOCLyRAIEqzH45O6p8Fv'
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key,q,limit=100,rating='g')
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = nextcord.Embed(tittle="with pleasure")
        emb.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await context.channel.send(embed=emb)

    except ApiException as e:
        print ("Exception when calling Api")

@bot.slash_command(name='gif')
async def gordon(context,*,q=''):
    api_key = 'SbnWbiNtkNyvcOCLyRAIEqzH45O6p8Fv'
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key,q,limit=100,rating='g')
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = nextcord.Embed(tittle="with pleasure")
        emb.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await context.channel.send(embed=emb)

    except ApiException as e:
        print ("Exception when calling Api")
        

@bot.slash_command(name='joke')
async def gordon(interaction: Interaction):
    await interaction.response.send_message(random.choice(weekly_jokes))
    
@bot.slash_command(name='whois')
async def gordon(ctx, member : nextcord.member):
    embed = nextcord.Embed (title = member.name , description = member.mention , color = nextcord.colour.blue())
    embed.add_field(name = "ID", value = member.id , inline = True)
    await interaction.response.send_message(embed=embed)

@bot.slash_command(name='sfw')
async def gordon(interaction: Interaction):
    await interaction.response.send_message(":black_large_square:Please keep chat safe for the minors, swear words or abbreviations related to swears are not allowed here.:black_large_square:")
    

bot.run(config.TOKEN)