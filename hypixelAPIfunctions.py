import requests
import json
from mojang import API
import datetime

session = requests.Session()
api = API(session = session)

def is_online(player_name, api_key):
    """Checks if a player is online on hypixel

    Args:
        player_name (string): The in game name of the player you wish to check
        api_key (string): Your api key

    Returns:
        Dict: returns the online status, and information about it
        Bool: If check fails, returns False
        Error: If this is returned, Contact Zmottos#4349
    """    
    try:
        player_uuid = api.get_uuid(player_name)
    except:
        return "Invalid name"
    url = f"https://api.hypixel.net/status?key={api_key}&uuid={player_uuid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        if data['session']['online'] == True:
            return(data)
        else:
            return False
    error = json.loads(response.content)
    return f"An error has occured: {error['cause']}. Contact Zmottos#4349 if you need help!"

def players_last_played(player_name, api_key):
    """Returns a dictonary containing information about the last played game of the player

    Args:
        player_name (string): The player you wish to key
        api_key (string): Your API key

    Returns:
        Dict: returns formation about the most recent played game
        Bool: If check fails, returns False
        Error: If this is returned, Contact Zmottos#4349
    """    
    try:
        players_uuid = api.get_uuid(player_name)
    except:
        return "Invalid name"
    url = f"https://api.hypixel.net/recentgames?key={api_key}&uuid={players_uuid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        if data["games"] != []:
            return(data["games"])
        else:
            return False
    error = json.loads(response.content)
    return f"An error has occured: {error['cause']}. Contact Zmottos#4349 if you need help!"

def get_limits(api_key):
    """Gets your limits on your key

    Args:
        api_key (string): Yourapi key

    Returns:
        string: Tells you your limits and how much uses left
    """    
    url = f"https://api.hypixel.net/key?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return f"Your limit is {data['record']['limit']} queries per minute, with {data['record']['limit'] - data['record']['queriesInPastMin']} left having used {data['record']['queriesInPastMin']} queries"
    else:
        error = json.loads(response.content)
        return error["cause"]

def convert_unix(unix):
    """Converts unix(MS) into a readable format

    Args:
        unix (number(int/float)): a unix number is milliseconds

    Returns:
        string: a more human formatted string
    """    
    unix_time_milliseconds = unix
    unix_time_seconds = unix_time_milliseconds / 1000.0
    readable_time = datetime.datetime.fromtimestamp(unix_time_seconds).strftime('%d-%m-%Y %H:%M')  # format as string
    return readable_time

def make_clean(TypeName):
    """Converts Type Names in the clean name version

    Args:
        TypeName (str): Games Type Name
    
    Returns:
        string: returns the clean name of the game
    """    
    if TypeName == "QUAKECRAFT":
        return "Quake"
    elif TypeName == "PAINTBALL":
        return "Paintball"
    elif TypeName == "SURVIVAL_GAMES":
        return "Blitz Survival Games"
    elif TypeName == "TNTGAMES":
        return "TNT Games"
    elif TypeName == "VAMPIREZ":
        return "VampireZ"
    elif TypeName == "WALLS3":
        return "Mega Walls"
    elif TypeName == "UHC":
        return "UHC Champions"
    elif TypeName == "MCGO":
        return "Cops and Crims"
    elif TypeName == "BATTLEGROUND":
        return "Warloads"
    elif TypeName == "SUPER_SMASH":
        return "Smash Heroes"
    elif TypeName == "GINGERBREAD":
        return "Turbo Kart Racers"
    elif TypeName == "SKYWARS":
        return "SkyWars"
    elif TypeName == "TRUE_COMBAT":
        return "Crazy Walls"
    elif TypeName == "SPEED_UHC":
        return "Speed UHC"
    elif TypeName == "SKYCLASH":
        return "SkyClash"
    elif TypeName == "LEGACY":
        return "Classic Games"
    elif TypeName == "BEDWARS":
        return "Bed Wars"
    elif TypeName == "SKYBLOCK":
        return "SkyBlock"
    elif TypeName == "SMP":
        return "SMP"
    elif TypeName == "WOOL_GAMES":
        return "Wool Wars"
    else:
        return TypeName.replace("_", " ").title()
