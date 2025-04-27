class PlayerAttributes:
    def __init__(self, health, mana, damage, armor):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.armor = armor

    def update_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0

    def update_mana(self, amount):
        self.mana += amount
        if self.mana < 0:
            self.mana = 0

    def __str__(self):
        return f"Health: {self.health}, Mana: {self.mana}, Damage: {self.damage}, Armor: {self.armor}"