class Card:
    def __init__(self, name, card_type, cost, effect):
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.effect = effect

class CardData:
    ATTACK_CARDS = [
        Card("Fireball", "Attack", 3, "Deal 5 damage to opponent."),
        Card("Lightning Strike", "Attack", 4, "Deal 7 damage to opponent."),
    ]

    DEFENSE_CARDS = [
        Card("Shield Block", "Defense", 2, "Reduce damage by 4."),
        Card("Healing Aura", "Defense", 3, "Restore 5 health."),
    ]

    UTILITY_CARDS = [
        Card("Mana Surge", "Utility", 2, "Gain 3 mana."),
        Card("Draw Power", "Utility", 1, "Draw 2 cards."),
    ]

    SPECIAL_CARDS = [
        Card("Time Warp", "Special", 5, "Take an extra turn."),
        Card("Meteor Shower", "Special", 6, "Deal 10 damage to all opponents."),
    ]

    @staticmethod
    def get_all_cards():
        return CardData.ATTACK_CARDS + CardData.DEFENSE_CARDS + CardData.UTILITY_CARDS + CardData.SPECIAL_CARDS

    @staticmethod
    def get_card_by_name(name):
        all_cards = CardData.get_all_cards()
        for card in all_cards:
            if card.name == name:
                return card
        return None