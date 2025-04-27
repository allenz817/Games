class AIOpponent:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = 8  # Base damage
        self.armor = 3   # Base armor

    def play_turn(self, player, card_system):
        """AI logic for playing cards and attacking"""
        # Simple AI strategy: prioritize healing if low on health
        if self.health < 30:
            # Look for healing cards
            healing_cards = [card for card in card_system.hand if "heal" in card.effect.lower()]
            if healing_cards:
                for card in healing_cards:
                    card_system.play_card(card)
                return
        
        # Otherwise, play attack cards
        attack_cards = [card for card in card_system.hand if card.card_type == "Attack"]
        if attack_cards:
            for card in attack_cards[:2]:  # Play up to 2 attack cards
                card_system.play_card(card)
        
        # Attack the player
        self.attack(player)
    
    def attack(self, player):
        """Attack the player using combat mechanics"""
        # Calculate damage (attacker's damage - defender's armor)
        damage_dealt = max(0, self.damage - player.armor)
        player.health -= damage_dealt
        print(f"AI attacks for {damage_dealt} damage! Player health: {player.health}")

    def play_card(self, player):
        """Legacy method for backward compatibility"""
        self.attack(player)