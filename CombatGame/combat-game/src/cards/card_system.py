from .card_data import CardData
from combat.mechanics import apply_card_effect

class CardSystem:
    def __init__(self):
        self.cards = CardData.get_all_cards()
        self.hand = []

    def draw_card(self):
        if self.cards:
            card = self.cards.pop(0)
            self.hand.append(card)
            return card
        return None

    def play_card(self, card, player=None, target=None):
        if card in self.hand:
            self.hand.remove(card)
            self.handle_card_effect(card, player, target)
            return True
        return False

    def handle_card_effect(self, card, player=None, target=None):
        """
        Handle the effect of a played card
        :param card: The card being played
        :param player: The player playing the card
        :param target: The target of the card effect
        """
        print(f"Playing {card.card_type} card: {card.name} - {card.effect}")
        
        if player:
            apply_card_effect(player, card, target)
        else:
            # Just print the card info if no player is provided
            if card.card_type == "Attack":
                print(f"Attack card: {card.name} - {card.effect}")
            elif card.card_type == "Defense":
                print(f"Defense card: {card.name} - {card.effect}")
            elif card.card_type == "Utility":
                print(f"Utility card: {card.name} - {card.effect}")
            elif card.card_type == "Special":
                print(f"Special card: {card.name} - {card.effect}")

    def shuffle_deck(self):
        import random
        random.shuffle(self.cards)
        return self.cards

    def reset_hand(self):
        self.hand = []