class Mana:
    def __init__(self, max_mana):
        self.current_mana = 0
        self.max_mana = max_mana

    def add_mana(self, amount):
        self.current_mana += amount
        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana

    def reset_mana(self):
        self.current_mana = 0

    def can_take_turn(self):
        return self.current_mana > 0

    def __str__(self):
        return f'Mana: {self.current_mana}/{self.max_mana}'