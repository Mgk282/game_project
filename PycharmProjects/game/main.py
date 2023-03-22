print("new game? Y/N")
game_start = input()
atacks_mob = True
if game_start == 'Y' or 'y' or 'н'or 'Н':
    atack_mob = int(input("kill mobs?"))
    if atack_mob == True:
        atacks_mob == True



class gg_warior:
    level = 1
    health = 100
    power = 30
    exp = 0
    damage = 25
    deff = 17
    exp_to_app = 100


class mob:
    level = 2
    health = 75
    damage = 9
    exp_drop = 12
    gold_drop = 4
    deff = 5
gg = gg_warior()
mobs = mob()

def atack(damage, deff):
    mobs.health -= (damage - deff)
    return mobs.health


kill = False


def fight(pers_one, pers_two):
    if gg.health > 0 and 0 >= mobs.health:
        kill = True
        return kill


if kill == True:
    if gg.exp == gg.exp_to_app:
        gg.level += 1
        gg.exp == 0
        gg.exp_to_app += 50
        mobs.level += 1
        mobs.gold_drop += 4
        mobs.health += 29
        mobs.exp_drop += 3
    else:
        gg.exp += mobs.exp_drop
if atacks_mob == True:
    while mobs.health > 0:
        atack(gg.damage, mobs.deff)
        atack(mobs.damage, gg.deff)
        print(mobs.health)
        fight(gg,mobs)
if kill == True:
    if gg.exp == gg.exp_to_app:
        gg.level += 1
        gg.exp == 0
        gg.exp_to_app += 50
        mobs.level += 1
        mobs.gold_drop += 4
        mobs.health += 29
        mobs.exp_drop += 3
    else:
        gg.exp += mobs.exp_drop
input()