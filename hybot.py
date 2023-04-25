import os
import discord
from discord import option
import dotenv
import hypixelAPIfunctions as hyapi
import hypixelreader as hr
import hybotFunctions as hf
ORBS = ["selene", "helios", "nyx", "zeus", "aphrodite", "archimedes", "hades", "Zmottos"]


dotenv.load_dotenv()
PATH = str(os.getenv("FILEPATH2"))
TOKEN = str(os.getenv("DISCORDTOKEN"))
KEY = str(os.getenv("APIKEY"))
bot = discord.Bot()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="hypixel"))

@bot.slash_command(name = "last_played", description = "Get stats of a player")
async def stats(ctx, name: str):
    await ctx.respond(f"Getting last played of {name}")
    info = hyapi.players_last_played(name,KEY)
    await ctx.edit(content = "API retrived, updating statement")
    try:
        data = [hyapi.convert_unix(info[0]['date']), info[0]['gameType']]
        await ctx.edit(content = f"{name}'s last played game was {hyapi.make_clean(data[1])} at {data[0]}")
    except:
        if info == False:
            await ctx.edit(content = f"{name}'s last played game is unknown! (Hasn't played recently or API off)")
            
        else:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: {info}")

@bot.slash_command(name = "fishing_stats", description = "Gets the fishing stats of the player" )
@option("name",
        description = "Enter the player's username")
@option("type",
        description = "Enter the type of stats you wish to view",
        choices = ["all", "lava", "water", "ice", "misc", "specials", "orbs"],
        default = "all")
async def fishing(ctx, 
                  name: str, 
                  type: str):
    await ctx.respond(f"Getting fishing stats of {name}")
    hr.get_player(name,KEY)
    data = hr.get_data(name)
    if data == -1:
        await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid Name")
    else:
        await ctx.edit(content = "Updated users stats, formatting")
        try:
            data = data['player']['stats']['MainLobby']['fishing']
        except:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid statistics")
            type = "Null"
    fish = 0
    junk = 0
    treasure = 0
    if type == "all":
        if "water" in data['stats']['permanent']:
            fish += data['stats']['permanent']['water']['fish']
            junk += data['stats']['permanent']['water']['junk']
            treasure += data['stats']['permanent']['water']['treasure']
        else:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid Stats")
            pass
        if fish != 0:
            if "lava" in data['stats']['permanent']:
                fish += data['stats']['permanent']['lava']['fish']
                junk += data['stats']['permanent']['lava']['junk']
                treasure += data['stats']['permanent']['lava']['treasure']
            if "ice" in data['stats']['permanent']:
                fish += data['stats']['permanent']['ice']['fish']
                junk += data['stats']['permanent']['ice']['junk']
                treasure += data['stats']['permanent']['ice']['treasure']
            if "orbs" in data:
                orbs = []
                for orb in ORBS:
                    orbs.append(hf.get_orbs(orb, data['orbs']))
                await ctx.edit(content = f"{name} has caught a total of:\n{fish} fish\n{treasure} treasure\n{junk} junk\n\nCaught orbs:\nSelene | {orbs[0]}\nHelios | {orbs[1]}\nNyx | {orbs[2]}\nZeus | {orbs[3]}\nAphrodite | {orbs[4]}\nArchimedes | {orbs[5]}\nHades | {orbs[6]}")
            else:
                await ctx.edit(content = f"{name} has caught a total of:\n{fish} fish\n{treasure} treasure\n{junk} junk\n\n{name} has no caught orbs")
    elif type == "water":
        if "water" in data['stats']['permanent']:
            fish = data['stats']['permanent']['water']['fish']
            junk = data['stats']['permanent']['water']['junk']
            treasure = data['stats']['permanent']['water']['treasure']
            await ctx.edit(content = f"{name}'s water fishing stats:\n{fish} fish\n{treasure} treasure\n{junk} junk")
    elif type == "lava":
        if "lava" in data['stats']['permanent']:
            fish = data['stats']['permanent']['lava']['fish']
            junk = data['stats']['permanent']['lava']['junk']
            treasure = data['stats']['permanent']['lava']['treasure']
            await ctx.edit(content = f"{name}'s lava fishing stats:\n{fish} fish\n{treasure} treasure\n{junk} junk")
        else:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid lava fishing stats")
    elif type == "ice":
        if "ice" in data['stats']['permanent']:
            fish = data['stats']['permanent']['ice']['fish']
            junk = data['stats']['permanent']['ice']['junk']
            treasure = data['stats']['permanent']['ice']['treasure']
            await ctx.edit(content = f"{name}'s ice fishing stats:\n{fish} fish\n{treasure} treasure\n{junk} junk")
        else:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid ice fishing stats")
    elif type == "misc":
        message = ""
        if "enchants" in data:
            if "lure" in data["enchants"]:
                message += f"Lure: {data['enchants']['lure']['level']}\n"
            if "luck" in data["enchants"]:
                message += f"Luck of the Sea: {data['enchants']['luck']['level']}\n"
            if "collector" in data["enchants"]:
                message += f"Collector: {data['enchants']['collector']['level']}\n"
            if "dumpster_diver" in data["enchants"]:
                message += f"Dumpster Diver: {data['enchants']['dumpster_diver']['level']}\n"
            if "vulcans_blessing" in data["enchants"]:
                message += f"Lava Fishing unlocked\n"
            if "neptunes_fury" in data["enchants"]:
                message += f"Ice Fishing unlocked\n\n"
        if "activeFishingRod" in data:
            message += f"{name} is currently using {data['activeFishingRod'].replace('_', ' ').title()}"
        await ctx.edit(content = f"{name}'s Misc fishings stats:\n{message}")
    elif type == "specials":
        message = ""
        if "special_fish" in data:
            message += f"{name} has caught {len(data['special_fish'])} special fish\n\n"
            specials = list(data['special_fish'].keys())
            for special in specials:
                message += f"{special.replace('_', ' ').title()} | ✓\n"
            await ctx.edit(content = message)
        else:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid special fishing stats")
    elif type == "orbs":
        if "orbs" in data:
            orbs = []
            for orb in ORBS:
                orbs.append(hf.get_orbs(orb, data['orbs']))
    
            await ctx.edit(content = f"{name} has caught the orbs:\nSelene | {orbs[0]}\nHelios | {orbs[1]}\nNyx | {orbs[2]}\nZeus | {orbs[3]}\nAphrodite | {orbs[4]}\nArchimedes | {orbs[5]}\nHades | {orbs[6]}\n\nhaving caught {sum(orbs)}")
        else:
            await ctx.edit(content = f"An Error occured while fetching data from {name}: Invalid orb fishing stats")


bot.run(TOKEN)