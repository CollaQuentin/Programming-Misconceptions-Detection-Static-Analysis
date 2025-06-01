class Weapon:
    def __init__(self, attack):
        self.attack = attack


class Cratos:
    def __init__(self, weapon):
        self.weapon = weapon

    def set_weapon(self, weapon):
        return self.weapon

    def hit(self, enemy):
        self.enemy = enemy
        return self.enemy


class Drauf:
    def __init__(self, life):
        self.life = life

    def get_hit(self, damage):
        return self.life - damage
