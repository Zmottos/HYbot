ORBS = ["selene", "helios", "nyx", "zeus", "aphrodite", "archimedes", "hades"]

def get_orbs(orb, orbs):
    if orb in orbs:
        return int(orbs[orb])
    else:
        return 0