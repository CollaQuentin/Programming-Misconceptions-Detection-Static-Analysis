class Weapon:
    def __init__(self,attack):
        self.attack=attack
class Cratos:
    def __init__(self,weapon):
        self.weapon=Weapon(attack)
    def set_weapon(self,weapon):
        self.weapon=Weapon(attack)
    def hit(self,enemy):
        enemy.life-=self.weapon
class Drauf:
    def __init__(self,life):
        self.life=life
    def get_hit(damage):
        self.life-=damage
