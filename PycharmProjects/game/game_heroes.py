class gg_warior:
    name = ""
    level = 1
    health = 100
    exp = 0
    damage = 25
    deff = 17
    exp_to_app = 100
    if exp >= exp_to_app:
        level += 1
        exp = 0
        exp_to_app += exp_to_app ** 2
        deff += 2
        health += health // 10 + 10
        damage += damage // 10 + 10
    gold = 0
    loot_damage = 0
    loot_deff = 0


class mob:
    level = 1
    health = 75
    damage = 9
    exp_drop = 12
    gold_drop = 4
    deff = 5
    if gg_warior.level > level:
        level += 1
        exp_drop += (exp_drop ** 2) - (exp_drop - exp_drop // 10)
        gold_drop += 2
        deff += deff * 2 -7


gg = gg_warior()
mobs = mob()
