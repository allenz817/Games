import pygame
import time
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
        self.player_turn_active = False
        self.ai_turn_active = False
        self.last_mana_update = 0
        self.mana_update_interval = 1.0  # Update mana every second

    def initialize_game(self):
        # Initialize player and AI attributes
        self.player = PlayerAttributes(health=100, mana=Mana(10), damage=10, armor=5)
        self.ai = AIOpponent(name="AI Opponent", health=100, mana=Mana(10))
        self.card_system = CardSystem()
        self.card_system.shuffle_deck()  # Shuffle the deck
        
        # Draw initial cards (5 cards)
        for _ in range(5):
            card = self.card_system.draw_card()
            print(f"Drew card: {card.name} ({card.card_type})")
            
        setup_layout()

    def game_loop(self):
        while not self.game_over:
            current_time = time.time()
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                
                # Handle player input during their turn
                if self.player_turn_active:
                    self.handle_player_input(event)
            
            # Update mana at regular intervals
            if current_time - self.last_mana_update >= self.mana_update_interval:
                self.update_mana()
                self.last_mana_update = current_time
            
            # Check if player's mana is full and it's not already their turn
            if self.player.mana.is_full() and not self.player_turn_active and not self.ai_turn_active:
                self.player_turn_active = True
                print("Player's turn started! Mana full.")
            
            # Check if AI's mana is full and it's not already their turn
            if self.ai.mana.is_full() and not self.player_turn_active and not self.ai_turn_active:
                self.ai_turn_active = True
                print("AI's turn started! Mana full.")
            
            # Draw the game screen
            card_rects, play_button_rect = draw_game_screen(self.player, self.ai, self.card_system)
            update_layout()
            
            # Check game status
            if is_game_over(self.player.health, self.ai.health):
                self.game_over = True
            
            # Control game speed
            self.clock.tick(30)

        self.check_game_status()

    def update_mana(self):
        """Update mana for both players"""
        self.player.mana.accumulate()
        self.ai.mana.accumulate()

    def handle_player_input(self, event):
        """Handle player input during their turn"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # Get the card rects and play button rect from the current frame
            card_rects, play_button_rect = draw_game_screen(self.player, self.ai, self.card_system)
            
            # Check if a card was clicked
            if handle_card_selection(pos, card_rects):
                print("Card selected!")
                
                # Validate card selection
                selected_cards = get_selected_cards()
                if len(selected_cards) > 1:
                    # Check if all selected cards are of the same type or if any are special
                    card_types = set(card.card_type for card in selected_cards)
                    has_special = "Special" in card_types
                    
                    if len(card_types) > 1 and not has_special:
                        print("You can only play cards of the same type or Special cards!")
                        # Deselect the last card
                        clear_selected_cards()
                        for card in selected_cards[:-1]:  # All but the last card
                            handle_card_selection((0,0), [(pygame.Rect(0,0,0,0), card)])
            
            # Check if play button was clicked
            elif play_button_rect and play_button_rect.collidepoint(pos):
                selected_cards = get_selected_cards()
                if selected_cards:
                    print("Playing selected cards!")
                    # Play all selected cards
                    for card in selected_cards:
                        self.card_system.play_card(card)
                    
                    clear_selected_cards()
                    self.player_turn_active = False  # End player's turn
                    self.player.mana.reset()  # Reset mana
                    
                    # Draw a new card
                    new_card = self.card_system.draw_card()
                    if new_card:
                        print(f"Drew new card: {new_card.name}")

    def ai_turn(self):
        """Handle AI's turn"""
        print("AI's turn!")
        self.ai.play_turn(self.player, self.card_system)
        self.ai_turn_active = False
        self.ai.mana.reset()  # Reset AI's mana

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