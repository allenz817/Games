from CombatGame.combat_game.src.cards.card_data import CardData

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

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.handle_card_effect(card)
            return True
        return False

    def handle_card_effect(self, card):
        if card.card_type == "Attack":
            print(f"Playing attack card: {card.name} - {card.effect}")
        elif card.card_type == "Defense":
            print(f"Playing defense card: {card.name} - {card.effect}")
        elif card.card_type == "Utility":
            print(f"Playing utility card: {card.name} - {card.effect}")
        elif card.card_type == "Special":
            print(f"Playing special card: {card.name} - {card.effect}")

    def shuffle_deck(self):
        import random
        random.shuffle(self.cards)

    def reset_hand(self):
        self.hand = []