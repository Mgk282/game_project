import PycharmProjects.game.game_heroes
from PycharmProjects.game.game_heroes import mobs, gg
kill = False

def atack(damage, deff):
    mobs.health -= (gg.damage - mobs.deff)
    print(PycharmProjects.game.game_heroes.mobs.health)
    return mobs.health

def kill_mob(pers_one, pers_two):
    if gg.health > 0 and 0 >= mobs.health:
       gg.exp += mobs.exp_drop



