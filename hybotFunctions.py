import json

def get_orbs(orb, orbs):
    if orb in orbs:
        return int(orbs[orb])
    else:
        return 0

def get_all_skywars(data):
    data = data['player']['stats']['SkyWars']
    info = []
    try:
        info.append(data['kills'])
        info.append(data['deaths'])
        info.append(data['wins'])
        info.append(data['losses'])
    except:
        return -1
    return info

def get_spec_skywars(data, position):
    data = data['player']['stats']['SkyWars']
    info = []
    try:
        info.append(data[f'kills_{position}'])
        info.append(data[f'deaths_{position}'])
        info.append(data[f'wins_{position}'])
        info.append(data[f'losses_{position}'])
    except:
        return -1
    return info

def parse_skywars_info(data, name, type):
    if data == -1:
        return f"An Error occured while fetching data from {name}: Invalid skywars stats"
    else:
        return f"{name}'s {type} stats \nKills: {data[0]} Deaths: {data[1]} KDR: {'%.2f' % (data[0] / data[1])}\nWins: {data[2]} Losses: {data[3]} W/R ratio: {'%.2f' % (data[2] / data[3])}"

if __name__ == "__main__":
    print("Function file")