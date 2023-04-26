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

if __name__ == "__main__":
    print("Function file")