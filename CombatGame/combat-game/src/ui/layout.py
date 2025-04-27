import pygame
import player

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Combat Game")
font = pygame.font.Font(None, 36)

def setup_layout():
    """
    Set up the main layout of the game.
    """
    screen.fill(WHITE)
    pygame.display.flip()

def draw_health_bar(player):
    """
    Draw the player's health bar on the screen.
    :param player: The player object whose health bar is being drawn.
    """
    health_percentage = player.health / 100
    health_bar_width = int(200 * health_percentage)
    pygame.draw.rect(screen, RED, (50, 50, 200, 20))  # Background bar
    pygame.draw.rect(screen, GREEN, (50, 50, health_bar_width, 20))  # Health bar
    health_text = font.render(f"Health: {player.health}/100", True, BLACK)
    screen.blit(health_text, (50, 80))

def draw_mana_bar(player):
    """
    Draw the player's mana bar on the screen.
    :param player: The player object whose mana bar is being drawn.
    """
    mana_percentage = player.mana.current / player.mana.max  # Access the mana attributes correctly
    mana_bar_width = int(200 * mana_percentage)
    pygame.draw.rect(screen, BLUE, (50, 120, 200, 20))  # Background bar
    pygame.draw.rect(screen, WHITE, (50, 120, mana_bar_width, 20))  # Mana bar
    mana_text = font.render(f"Mana: {player.mana.current}/{player.mana.max}", True, BLACK)
    screen.blit(mana_text, (50, 150))

def display_card_hand(player):
    """
    Display the player's hand of cards.
    :param player: The player object whose cards are being displayed.
    """
    x, y = 50, 200  # Starting position for cards
    for card in player.card_system.hand:
        card_text = font.render(f"{card.name} ({card.card_type})", True, BLACK)
        screen.blit(card_text, (x, y))
        y += 40  # Move down for the next card

def position_elements():
    """
    Position UI elements based on screen size.
    """
    # This function can be used to dynamically adjust positions if needed
    pass

def update_layout():
    """
    Update the layout dynamically during gameplay.
    """
    pygame.display.flip()