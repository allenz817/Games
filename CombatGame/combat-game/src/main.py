import pygame
from player.attributes import PlayerAttributes
from player.mana import Mana
from cards.card_system import CardSystem
from combat.ai_opponent import AIOpponent
from combat.mechanics import is_game_over
from ui.layout import setup_layout, draw_health_bar, draw_mana_bar, display_card_hand, update_layout

class Game:
    def __init__(self):
        self.player = None
        self.ai = None
        self.card_system = None
        self.game_over = False
        self.clock = pygame.time.Clock()

    def initialize_game(self):
        # Initialize player and AI attributes
        self.player = PlayerAttributes(health=100, mana=Mana(10), damage=10, armor=5)
        self.ai = AIOpponent(name="AI Opponent", health=100, mana=Mana(10))
        self.card_system = CardSystem()
        self.card_system.cards = CardSystem().shuffle_deck()
        setup_layout()

    def game_loop(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            # Player's turn
            self.player_turn()
            if is_game_over(self.player.health, self.ai.health):
                self.game_over = True
                break

            # AI's turn
            self.ai_turn()
            if is_game_over(self.player.health, self.ai.health):
                self.game_over = True

            # Update the screen
            update_layout()
            self.clock.tick(30)  # Limit to 30 FPS

        self.check_game_status()

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
        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.initialize_game()
    game.game_loop()