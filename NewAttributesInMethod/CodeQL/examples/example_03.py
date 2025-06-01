class Weapon:
    def __init__(self, attack=0):
        self.attack = attack

class Cratos:
    def __init__(self,weapon=None):
        self.weapon = weapon
    def set_weapon(weapon):
        self.weapon = weapon
    def hit(enemy,life):
        enemy.get_hit(self.weapon)

class Drauf:
    def __init__(self,life=0):
        self.life = life
    def get_hit(damage):
        self.damage=damage
        self.life= self.life-damage
