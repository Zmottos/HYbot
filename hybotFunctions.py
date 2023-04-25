def get_orbs(orb, orbs):
    if orb in orbs:
        return int(orbs[orb])
    else:
        return 0
    
def get_lab_solo(data):
    data = data['player']['stats']['SkyWars']
    info = []
    info.append(data['deaths_lab_solo'])
    info.append(data['time_played_lab_solo'])
    info.append(data['kills_lab_solo'])
    info.append(data['wins_lab_solo'])
    info.append(data['losses_lab_solo'])
    return info

def get_lab_teams(data):
    info = []
    info.append(data['deaths_lab_teams'])
    info.append(data['time_played_lab_teams'])
    info.append(data['kills_lab_teams'])
    info.append(data['wins_lab_teams'])
    info.append(data['losses_lab_teams'])
    return info

    
if __name__ == "__main__":
    print("Function file")