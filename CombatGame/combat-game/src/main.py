from CombatGame.combat_game.src.player.attributes import PlayerAttributes
from CombatGame.combat_game.src.player.mana import Mana
from CombatGame.combat_game.src.cards.card_system import CardSystem
from CombatGame.combat_game.src.combat.ai_opponent import AIOpponent
from CombatGame.combat_game.src.combat.mechanics import calculate_damage, is_game_over
from CombatGame.combat_game.src.ui.layout import draw_health_bar, draw_mana_bar, display_card_hand

class Game:
    def __init__(self):
        self.player = None
        self.ai = None
        self.card_system = None
        self.game_over = False

    def initialize_game(self):
        # Initialize player and AI attributes
        self.player = PlayerAttributes(health=100, mana=Mana(10), damage=10, armor=5)
        self.ai = AIOpponent(name="AI Opponent", health=100, mana=Mana(10))
        self.card_system = CardSystem()
        self.card_system.cards = CardSystem().shuffle_deck()

    def game_loop(self):
        while not self.game_over:
            self.player_turn()
            if is_game_over(self.player.health, self.ai.health):
                self.game_over = True
                break
            self.ai_turn()
            if is_game_over(self.player.health, self.ai.health):
                self.game_over = True

    def player_turn(self):
        print("Player's turn!")
        draw_health_bar(self.player)
        draw_mana_bar(self.player)
        display_card_hand(self.player)
        # Add logic for player to play cards and attack

    def ai_turn(self):
        print("AI's turn!")
        self.ai.play_card(self.player)

    def check_game_status(self):
        if self.player.health <= 0:
            print("Game Over! AI wins!")
        elif self.ai.health <= 0:
            print("Game Over! Player wins!")

if __name__ == "__main__":
    game = Game()
    game.initialize_game()
    game.game_loop()