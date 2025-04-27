class AIOpponent:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
        self.cards = []  # List to hold AI's cards

    def draw_card(self, card):
        self.cards.append(card)

    def play_card(self, player):
        if self.cards:
            # Simple strategy: play the first card available
            card = self.cards.pop(0)
            self.execute_card(card, player)

    def execute_card(self, card, player):
        if card.type == 'Attack':
            damage = card.effect
            player.health -= damage
            print(f"{self.name} attacks {player.name} for {damage} damage!")
        elif card.type == 'Defense':
            # Implement defense logic
            pass
        elif card.type == 'Utility':
            # Implement utility logic
            pass
        elif card.type == 'Special':
            # Implement special card logic
            pass

    def decide_action(self, player):
        # Basic decision-making based on player health and available cards
        if player.health < 20:
            # If player is low on health, prioritize attack
            self.play_card(player)
        else:
            # Otherwise, play a card based on availability
            self.play_card(player)