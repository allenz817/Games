class Mana:
    def __init__(self, max_mana):
        self.current = 0  # Start with 0 mana
        self.max = max_mana
        self.accumulation_rate = 1  # Mana gained per update

    def accumulate(self):
        """Accumulate mana over time"""
        self.current += self.accumulation_rate
        if self.current > self.max:
            self.current = self.max
        return self.is_full()

    def is_full(self):
        """Check if mana is full"""
        return self.current >= self.max

    def reset(self):
        """Reset mana after taking a turn"""
        self.current = 0

    def __str__(self):
        return f'Mana: {self.current}/{self.max}'