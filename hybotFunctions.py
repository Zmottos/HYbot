ORBS = ["selene", "helios", "nyx", "zeus", "aphrodite", "archimedes", "hades"]

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