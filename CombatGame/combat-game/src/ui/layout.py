import pygame

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)

# Card dimensions
CARD_WIDTH = 120
CARD_HEIGHT = 160
CARD_SPACING = 20

# Button dimensions
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Combat Game")
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Keep track of selected cards
selected_cards = []

def setup_layout():
    """
    Set up the main layout of the game.
    """
    screen.fill(WHITE)
    pygame.display.flip()

def draw_player(player, is_human=True):
    """
    Draw a player character on the screen.
    :param player: The player object to draw
    :param is_human: True if this is the human player, False for AI
    """
    # Position players on left (human) and right (AI) sides
    x = 150 if is_human else SCREEN_WIDTH - 150
    y = SCREEN_HEIGHT // 2
    
    # Draw a simple avatar for now (circle with color)
    color = BLUE if is_human else RED
    pygame.draw.circle(screen, color, (x, y), 50)
    
    # Draw player name
    name = "Player" if is_human else "AI Opponent"
    name_text = font.render(name, True, BLACK)
    name_rect = name_text.get_rect(center=(x, y + 80))
    screen.blit(name_text, name_rect)

def draw_health_bar(player, is_human=True):
    """
    Draw the player's health bar on the screen.
    :param player: The player object whose health bar is being drawn.
    :param is_human: True if this is the human player, False for AI
    """
    x = 50 if is_human else SCREEN_WIDTH - 250
    
    health_percentage = player.health / 100
    health_bar_width = int(200 * health_percentage)
    pygame.draw.rect(screen, RED, (x, 50, 200, 20))  # Background bar
    pygame.draw.rect(screen, GREEN, (x, 50, health_bar_width, 20))  # Health bar
    health_text = font.render(f"Health: {player.health}/100", True, BLACK)
    screen.blit(health_text, (x, 80))

def draw_mana_bar(player, is_human=True):
    """
    Draw the player's mana bar on the screen.
    :param player: The player object whose mana bar is being drawn.
    :param is_human: True if this is the human player, False for AI
    """
    x = 50 if is_human else SCREEN_WIDTH - 250
    
    mana_percentage = player.mana.current / player.mana.max
    mana_bar_width = int(200 * mana_percentage)
    pygame.draw.rect(screen, BLUE, (x, 120, 200, 20))  # Background bar
    pygame.draw.rect(screen, LIGHT_BLUE, (x, 120, mana_bar_width, 20))  # Mana bar
    mana_text = font.render(f"Mana: {player.mana.current}/{player.mana.max}", True, BLACK)
    screen.blit(mana_text, (x, 150))

def display_card_hand(card_system):
    """
    Display the player's hand of cards at the bottom of the screen.
    :param card_system: The CardSystem object managing the player's cards.
    :return: List of card rects for hit detection
    """
    card_rects = []
    
    # Calculate starting position to center cards
    total_width = min(5, len(card_system.hand)) * (CARD_WIDTH + CARD_SPACING) - CARD_SPACING
    start_x = (SCREEN_WIDTH - total_width) // 2
    y = SCREEN_HEIGHT - CARD_HEIGHT - 80
    
    # Draw up to 5 cards
    for i, card in enumerate(card_system.hand[:5]):
        x = start_x + i * (CARD_WIDTH + CARD_SPACING)
        
        # Determine card color based on type and selection state
        card_color = WHITE
        if card in selected_cards:
            # Selected cards appear raised
            y_offset = -20
        else:
            y_offset = 0
            
        if card.card_type == "Attack":
            border_color = RED
        elif card.card_type == "Defense":
            border_color = GREEN
        elif card.card_type == "Utility":
            border_color = BLUE
        else:  # Special
            border_color = LIGHT_BLUE
            
        # Draw card background
        card_rect = pygame.Rect(x, y + y_offset, CARD_WIDTH, CARD_HEIGHT)
        pygame.draw.rect(screen, card_color, card_rect)
        pygame.draw.rect(screen, border_color, card_rect, 3)  # Border
        
        # Draw card name
        name_text = small_font.render(card.name, True, BLACK)
        name_rect = name_text.get_rect(center=(x + CARD_WIDTH//2, y + y_offset + 30))
        screen.blit(name_text, name_rect)
        
        # Draw card type
        type_text = small_font.render(card.card_type, True, BLACK)
        type_rect = type_text.get_rect(center=(x + CARD_WIDTH//2, y + y_offset + 60))
        screen.blit(type_text, type_rect)
        
        # Draw card effect
        effect_lines = [card.effect[i:i+15] for i in range(0, len(card.effect), 15)]
        for j, line in enumerate(effect_lines[:3]):
            effect_text = small_font.render(line, True, BLACK)
            effect_rect = effect_text.get_rect(center=(x + CARD_WIDTH//2, y + y_offset + 90 + j*20))
            screen.blit(effect_text, effect_rect)
        
        card_rects.append((card_rect, card))
    
    return card_rects

def draw_play_button():
    """
    Draw the play button for playing selected cards.
    :return: Button rect for hit detection
    """
    button_x = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
    button_y = SCREEN_HEIGHT - 60
    
    button_rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    
    # Button changes color if cards are selected
    if selected_cards:
        pygame.draw.rect(screen, GREEN, button_rect)
    else:
        pygame.draw.rect(screen, GRAY, button_rect)
    
    pygame.draw.rect(screen, BLACK, button_rect, 2)  # Border
    
    # Button text
    button_text = font.render("PLAY", True, BLACK)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)
    
    return button_rect

def handle_card_selection(pos, card_rects):
    """
    Handle card selection based on mouse click.
    :param pos: Mouse position (x, y)
    :param card_rects: List of (rect, card) tuples
    :return: True if a card was selected/deselected
    """
    global selected_cards
    
    for rect, card in card_rects:
        if rect.collidepoint(pos):
            if card in selected_cards:
                selected_cards.remove(card)
            else:
                selected_cards.append(card)
            return True
    
    return False

def get_selected_cards():
    """
    Get the currently selected cards.
    :return: List of selected card objects
    """
    return selected_cards.copy()

def clear_selected_cards():
    """
    Clear the list of selected cards.
    """
    global selected_cards
    selected_cards = []

def draw_game_screen(player, ai, card_system):
    """
    Draw the complete game screen.
    :param player: The human player
    :param ai: The AI player
    :param card_system: The card system
    :return: Tuple of (card_rects, play_button_rect)
    """
    screen.fill(WHITE)
    
    # Draw players
    draw_player(player, is_human=True)
    draw_player(ai, is_human=False)
    
    # Draw health and mana bars
    draw_health_bar(player, is_human=True)
    draw_mana_bar(player, is_human=True)
    draw_health_bar(ai, is_human=False)
    draw_mana_bar(ai, is_human=False)
    
    # Draw cards and play button
    card_rects = display_card_hand(card_system)
    play_button_rect = draw_play_button()
    
    return card_rects, play_button_rect

def update_layout():
    """
    Update the layout dynamically during gameplay.
    """
    pygame.display.flip()