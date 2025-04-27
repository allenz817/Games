import pygame
from player.attributes import PlayerAttributes
from player.mana import Mana
from cards.card_system import CardSystem
from combat.ai_opponent import AIOpponent
from combat.mechanics import is_game_over
from ui.layout import setup_layout, draw_game_screen, update_layout, handle_card_selection, get_selected_cards, clear_selected_cards

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
        self.card_system.shuffle_deck()  # Shuffle the deck
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
        player_turn_active = True
        card_rects = None
        play_button_rect = None

        while player_turn_active:
            # Draw the game screen
            card_rects, play_button_rect = draw_game_screen(self.player, self.ai, self.card_system)
            update_layout()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    player_turn_active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Example: End turn with SPACE key
                        player_turn_active = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    
                    # Check if a card was clicked
                    if card_rects and handle_card_selection(pos, card_rects):
                        print("Card selected!")
                    
                    # Check if play button was clicked
                    elif play_button_rect and play_button_rect.collidepoint(pos) and get_selected_cards():
                        print("Playing selected cards!")
                        # Play all selected cards
                        for card in get_selected_cards():
                            self.card_system.play_card(card)
                        
                        clear_selected_cards()
                        player_turn_active = False  # End turn after playing cards
            
            # Control game speed
            self.clock.tick(30)

    def ai_turn(self):
        print("AI's turn!")
        # AI logic to play cards or attack
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