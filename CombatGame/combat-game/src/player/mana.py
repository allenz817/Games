class Mana:
    def __init__(self, max_mana):
        self.current = 0  # Renamed from current_mana to current
        self.max = max_mana  # Renamed from max_mana to max

    def add_mana(self, amount):
        self.current += amount
        if self.current > self.max:
            self.current = self.max

    def reset(self):
        self.current = 0  # Renamed reset_mana to reset

    def can_take_turn(self):
        return self.current > 0

    def __str__(self):
        return f'Mana: {self.current}/{self.max}'