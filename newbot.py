import email
from turtle import title
import nextcord
from nextcord import Intents, Interaction, Member
import os
from nextcord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random
from nextcord.enums import ContentFilter
from nextcord import member

testserverid = 949663512089735219

jokes = ["Some cause happiness wherever they go, others whenever they go","I can’t believe I got fired from the calendar factory. All I did was take a day off","I spent the last 2 years looking for my ex girlfriend's killer...... ||no one will do it||"
,"There are immigrants who came to your country that stole jobs and murdered the local population, we call those immigrants the founding fathers","I went to a party one day and Brad Pitt was there, they say never meet your heroes but i think Brad handled it really well","I was involved in a one night stand that went horribly wrong, we've been married 3 years now","My therapist says I'm addicted to revenge. We’ll see about that","Most people are shocked when they find out i'm not a good elctrician","Never judge someone till you walk a mile in their shoes, that way when you do judge them you'll be a mile away and have their shoes","The man who invented Velcro has died. RIP.","I have a few jokes about unemployed people, but none of them work."]

intents =nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.slash_command
async def test(interaction: Interaction):
    emb = nextcord.Embed(
        title="Testing embeds",
        color = 0x5460e7
    )
    emb.set_image(url="https://jangorecipes.com/wp-content/uploads/2021/04/image-2-1.jpg")
    await interaction.send(embed=emb)


@bot.slash_command
async def burger(interaction: Interaction):
    emb = nextcord.Embed(
        title="I can tell that you are not a fan of dieting" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://popmenucloud.com/cdn-cgi/image/width=1200,height=1200,fit=scale-down,format=auto,quality=60/pnkdlobe/dbe27b78-ff01-4b4f-8ea3-44b2fbc7467c.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def fishnchips(interaction: Interaction):
    emb = nextcord.Embed(
        title="What in broken teabags is that!, go back to britain pls" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://media-cdn.tripadvisor.com/media/photo-s/0e/8c/d9/3a/ticket-da-british-airways.jpg")
    await interaction.send(embed=emb)
   
@bot.slash_command
async def potato(interaction: Interaction):
    emb = nextcord.Embed(
        title="Do i look like a {words reserved for the real gordon} farmers market to you!" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def chicken(interaction: Interaction):
    emb = nextcord.Embed(
        title="Please ask for kfc please chicken isn't specific enough" ,
        color = 0x5460e7
    )
    
    await interaction.send(embed=emb)

@bot.slash_command
async def fish(interaction: Interaction):
    emb = nextcord.Embed(
        title="Wait! wait! what kind is it?, smoked, baked? fried?, make up your mind then come talk to me" ,
        color = 0x5460e7
    )
    
    await interaction.send(embed=emb)

@bot.slash_command
async def wine(interaction: Interaction):
    emb = nextcord.Embed(
        title="sry i dont serve alcoholics" ,
        color = 0x5460e7
    )
    
    await interaction.send(embed=emb)

@bot.slash_command
async def weed(interaction: Interaction):
    emb = nextcord.Embed(
        title="Whoah! lets not go there buddy" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://image.shutterstock.com/image-photo/closeup-portrait-shocked-mad-young-260nw-171534797.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def kfc(interaction: Interaction):
    emb = nextcord.Embed(
        title="Here u go plateful of kentucky fried crap" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://media-cdn.tripadvisor.com/media/photo-p/1c/11/af/0a/kfc.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def icecream(interaction: Interaction):
    emb = nextcord.Embed(
        title="You want some sprinkles with that" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.seriouseats.com/thmb/pBfRgXDTVM83cFPofomuEB4U5r4=/386x386/smart/filters:no_upscale()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2012__07__20120712-214287-blue-moon-ice-cream-674defba6e0f45ec97dc7eefa40ff6c1.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def pizza(interaction: Interaction):
    emb = nextcord.Embed(
        title="I hope you like pineapples" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url='https://d332juqdd9b8hn.cloudfront.net/wp-content/uploads/2019/07/GettyImages-487260560.jpg')
    await interaction.send(embed=emb)

@bot.slash_command
async def chocalate(interaction: Interaction):
    emb = nextcord.Embed(
        title="Straight from an overpriced duty free that imports stuff from belgium" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://helios-i.mashable.com/imagery/articles/03mEQzADyVpfAdgerKolpDJ/images-2.fit_lim.size_2000x.v1643400228.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def milo(interaction: Interaction):
    emb = nextcord.Embed(
        title="Lemme guess you a cricket fan?" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/12539919_XL1_20210208.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def brownie(interaction: Interaction):
    emb = nextcord.Embed(
        title="Please try soaking this in vannila ice cream" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://preppykitchen.com/wp-content/uploads/2019/10/Brownie-Recipe-Square-1200px-preppy-kitchen.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def fries(interaction: Interaction):
    emb = nextcord.Embed(
        title="The cause for your heart burn is here!!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://images.immediate.co.uk/production/volatile/sites/30/2021/03/French-fries-b9e3e0c.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def kottu(interaction: Interaction):
    emb = nextcord.Embed(
        title="Takata! Takata! Tak! Tak! Tak!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://limitlessspice.com/wp-content/uploads/2022/02/kottu-g734b601c4_1920-500x375.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def boba(interaction: Interaction):
    emb = nextcord.Embed(
        title="Drink it slowly ok!, I don't have time for refils" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://mamalikestocook.com/wp-content/uploads/2021/04/feature-blue-boba-milk-tea.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def pudding(interaction: Interaction):
    emb = nextcord.Embed(
        title="Woah! woah!, what kind is it?, figi or some other kind of pudding that i have defintely not forgotten" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def vivs(interaction: Interaction):
    emb = nextcord.Embed(
        title="Sorry i'm not allowed to serve garbage to people" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def shen(interaction: Interaction):
    emb = nextcord.Embed(
        title="One simp coming up!" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def ima(interaction: Interaction):
    emb = nextcord.Embed(
        title="Sorry i' don't have that try looking in a mental facility" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def nehan(interaction: Interaction):
    emb = nextcord.Embed(
        title="Umm try looking in the toilet, or maybe sewer" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def tea(interaction: Interaction):
    emb = nextcord.Embed(
        title="One lump or two?" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.aicr.org/wp-content/uploads/2020/06/peppermint-tea-on-teacup-1417945-1200x826.jpg.webp")
    await interaction.send(embed=emb)

@bot.slash_command
async def burrito(interaction: Interaction):
    emb = nextcord.Embed(
        title="I've got you covered fam" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/60/Burrito.JPG")
    await interaction.send(embed=emb)

@bot.slash_command
async def subway(interaction: Interaction):
    emb = nextcord.Embed(
        title="We call it soubway here dude, we don't do that here" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://c.tenor.com/fBvQV_5Lp6UAAAAC/we-dont-do-that-here-black-panther.gif")
    await interaction.send(embed=emb)

@bot.slash_command
async def coffee(interaction: Interaction):
    emb = nextcord.Embed(
        title="Burnin that mid night oil?" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/flat-white-d8ada0f.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def yes(interaction: Interaction):
    emb = nextcord.Embed(
        title="Ok here you go!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://flyclipart.com/thumb2/sparkle-sparkles-star-starred-starring-stars-icon-165986.png")
    await interaction.send(embed=emb)

@bot.slash_command
async def no(interaction: Interaction):
    emb = nextcord.Embed(
        title="Alright, but's gonna taste pretty bland though" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.pikpng.com/pngl/m/161-1617713_rolling-eyes-emoji-copy-emoji-ojos-en-blanco.png")
    await interaction.send(embed=emb)

@bot.slash_command
async def taco(interaction: Interaction):
    emb = nextcord.Embed(
        title="taco bell no tiene nada en mi" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://img.taste.com.au/w_-0kcUJ/taste/2016/11/aussie-style-beef-and-salad-tacos-86525-1.jpeg")
    await interaction.send(embed=emb)

@bot.slash_command
async def cake(interaction: Interaction):
    emb = nextcord.Embed(
        title="Hope theres a gym near your place, no one can resist my grandma's recipe" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://retiredblokeonfoodnstuff.files.wordpress.com/2018/11/imgp4014-tue-27th-nutty-blue-cake-slice-for-school-6.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def pancake(interaction: Interaction):
    emb = nextcord.Embed(
        title="Alright, but then who gets the milkshake?" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.delscookingtwist.com/wp-content/uploads/2022/01/Easy-Fluffy-American-Pancakes_1.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def milkshake(interaction: Interaction):
    emb = nextcord.Embed(
        title="Oh, it was you!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://levoque.co.za/image/cache/catalog/FlavourImages/bluemilkshake-500x500.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def cola(interaction: Interaction):
    emb = nextcord.Embed(
        title="Comin right up!, btw if u saw that experiment where they put this in an egg for 24 hours it was a fake" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://images.indianexpress.com/2021/07/GettyImages-drink-beverage-coca-cola-1200.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def lolipop(interaction: Interaction):
    emb = nextcord.Embed(
        title="Man, your dentist is gonan get rich... well, RICHER" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://wallpaperaccess.com/full/196127.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def biriyani(interaction: Interaction):
    emb = nextcord.Embed(
        title="Here you go, straight from nehan's kitchen" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.sponge.lk/images/products/PHK1009_0.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def imeth(interaction: Interaction):
    emb = nextcord.Embed(
        title="Some things are just too good for poeple to have" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.sponge.lk/images/products/PHK1009_0.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def cookie(interaction: Interaction):
    emb = nextcord.Embed(
        title="Right out of the google search bar just for you!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.cookingclassy.com/wp-content/uploads/2014/06/chocolate-chip-cookie-16.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def hello(interaction: Interaction):
    emb = nextcord.Embed(
        title="Hai!!!!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://cdn.discordapp.com/emojis/726161121446330438.gif")
    await interaction.send(embed=emb)

@bot.slash_command
async def one(interaction: Interaction):
    emb = nextcord.Embed(
        title="One lump on ur head it is!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://tenor.com/view/minion-bonk-hammer-minions-despicable-me-gif-5290684")
    await interaction.send(embed=emb)

@bot.slash_command
async def two(interaction: Interaction):
    emb = nextcord.Embed(
        title="Two? sure lemme grab my club" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://media4.giphy.com/media/30lxTuJueXE7C/giphy.gif")
    await interaction.send(embed=emb)

@bot.slash_command
async def lasagna(interaction: Interaction):
    emb = nextcord.Embed(
        title="Quick! take it!, before garfieldcomes back!!!" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.thewholesomedish.com/wp-content/uploads/2018/07/Best-Lasagna-550-500x375.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def donut(interaction: Interaction):
    emb = nextcord.Embed(
        title="-INSERT COP JOKE HERE-" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def pasta(interaction: Interaction):
    emb = nextcord.Embed(
        title="I can't think of anything italian to say so here" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://assets.bonappetit.com/photos/5b9a901947aaaf7cd9ea90f2/2:3/w_1874,h_2811,c_limit/ba-recipe-pasta-al-limone.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def hotdog(interaction: Interaction):
    emb = nextcord.Embed(
        title="You know if you eat enough of these the term suasage fest will be safe for work" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://iambaker.net/wp-content/uploads/2019/07/BuffaloHotDogs1-blog.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def salad(interaction: Interaction):
    emb = nextcord.Embed(
        title="I'm guessing you looked in a mirror?" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="")
    await interaction.send(embed=emb)

@bot.slash_command
async def salmon(interaction: Interaction):
    emb = nextcord.Embed(
        title="Getting fancy aren't we?, seriously are you tryna hunt bears or something?" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.wholesomeyum.com/wp-content/uploads/2021/06/wholesomeyum-Pan-Seared-Salmon-Recipe-13.jpg")
    await interaction.send(embed=emb)

@bot.slash_command
async def scallops(interaction: Interaction):
    emb = nextcord.Embed(
        title="One sec, BLUE TEAM WTF ARE YOU DOING THE SCALLOPS ARE RAW!!!!, yeah your scallops will be right out" ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def ping(interaction: Interaction):
    ping = (f'Ping: {round(bot.latency * 1000)}ms')
    emb = nextcord.Embed(
        title= ping ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
async def sfw(interaction: Interaction):
    emb = nextcord.Embed(
        title="This is a sfw work server, please do not post pornographic media" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://www.pinclipart.com/picdir/middle/545-5451200_no-symbol-computer-icons-clip-art-red-no.png")
    await interaction.send(embed=emb)
    
@bot.slash_command
async def joke(interaction: Interaction):
    rand = (random.choice(jokes))
    emb = nextcord.Embed(
        title=rand ,
        color = 0x5460e7
    )
    await interaction.send(embed=emb)

@bot.slash_command
@commands.has_permissions(kick_members=True)
async def kick(interaction: Interaction): 
    nextcord.Member.kick
    await interaction.response.send_message(f'{Member} Was bonked out of this server.')
    

@bot.slash_command
async def nilen(interaction: Interaction):
    emb = nextcord.Embed(
        title="one simp coming up!. wait i used that before, i mean i would call this an idiot but that was would an insult to stupid ppl" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://cdn.discordapp.com/emojis/947137866721554473.webp?size=60&quality=lossless")
    await interaction.send(embed=emb)

@bot.slash_command
async def dison(interaction: Interaction):
    emb = nextcord.Embed(
        title="If you wanted faliure you should have asked for my son but i guess this is good" ,
        color = 0x5460e7
    )
    emb.set_thumbnail(url="https://cdn.discordapp.com/emojis/894465344092139550.webp?size=60&quality=lossless")
    await interaction.send(embed=emb)



bot.run("ODAwNjA0MjgwNzU0Mjc0MzA2.YAUi1w.SapzrfWRys6i-qQ5zPoSTBOxc7E")


