import os
import dotenv
import time
import random
import requests
import json
from mojang import API


dotenv.load_dotenv()
PATH = str(os.getenv("FILEPATH2"))
KEY = str(os.getenv("APIKEY"))

session = requests.Session()
api = API(session = session)

def get_player(name,api_key):
    """Adds a player to the data text doc

    Args:
        name (string): The username of the player attempting to be checked
        api_key (string): an api key gotten from hypixel

    Returns:
        string: informing the user of what happened
        integer: returns -1 for invalid usernames
        boolean: return True if an error occurs
    """    
    new = True
    update = False
    count = 0
    t = time.time()
    t = int(t)+random.randint(0,1)

    try:
        player_uuid = api.get_uuid(name)
    except:
        return -1


    with open(PATH, "r") as f:
        for line in f:
            if name.lower() in line[:17].lower():
                if t - int(line[17:27]) < 300:
                    new = False
                    break
                else:
                    update = True
                    break
            count += 1
        else:
            count = -1

    if new == False:
        return "That player has been already been updated!"
    with open(PATH, "r") as f:
        data = f.readlines()

    if update == True:
        url = f"https://api.hypixel.net/player?key={api_key}&uuid={player_uuid}"
        response = requests.get(url)
        stats = json.loads(response.content)
        data[count] = f"{name} {' ' * (16-len(name))}{t}:{json.dumps(stats)}\n"


    if new == True and update == True:
        with open(PATH, "w", encoding="utf-8") as f:
            f.writelines(data)
            return f"Updated stats for {name}"

    if count == -1:
        url = f"https://api.hypixel.net/player?key={api_key}&uuid={player_uuid}"
        response = requests.get(url)
        stats = json.loads(response.content)
        with open(PATH, "a", encoding ="utf-8") as f:
            f.write(f"{name} {' ' * (16-len(name))}{t}:{json.dumps(stats)}\n")
        return f"Added new player {name}"
    return True

def get_data(name):
    """Parses data from the data file

    Args:
        name (string): name of the player who's data you're getting

    Returns:
        dict: a dictionary of the player's data
    """    
    with open(PATH, "r") as f:
        for line in f:
            if name.lower() in line[:17].lower():
                return json.loads(line[28:])
