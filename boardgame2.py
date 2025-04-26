import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Board and player setup
board = ["Start", "Property A", "Chance", "Property B", "Tax", "Property C", 
         "Go to Jail", "Free Parking", "Chance 2", "Property D",
         "Property E", "Community Chest", "Luxury Tax", "Railroad", "Utility",
            "Property F"]


block_positions = [(100 + i * 100, 500) for i in range(4)] + \
                  [(500, 500 - i * 100) for i in range(4)] + \
                  [(500 - i * 100, 100) for i in range(4)] + \
                  [(100, 100 + i * 100) for i in range(4)]

player_position = 0
player_money = 1500
player_icon = pygame.image.load("player_icon.png")
player_icon = pygame.transform.scale(player_icon, (40, 40))

# Dice function
def roll_dice():
    return random.randint(1, 6)

# Draw the board
def draw_board():
    for i, pos in enumerate(block_positions):
        pygame.draw.rect(screen, BLUE if i % 2 == 0 else GREEN, (*pos, 80, 80))
        font = pygame.font.Font(None, 24)
        text = font.render(board[i], True, WHITE)
        screen.blit(text, (pos[0] + 5, pos[1] + 5))

# Draw the player
def draw_player(position):
    x, y = block_positions[position]
    screen.blit(player_icon, (x + 20, y + 20))
    
def draw_button():
    button_rect = pygame.Rect(WIDTH - 200, HEIGHT - 100, 100, 50)
    pygame.draw.rect(screen, RED, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Roll Dice", True, WHITE)
    screen.blit(text, (button_rect.x + 10, button_rect.y + 10))
    return button_rect

# Function to animate player movement
def animate_player_movement(start_position, steps):
    global player_position
    for step in range(1, steps + 1):
        # Calculate the next position
        player_position = (start_position + step) % len(board)
        
        # Redraw the screen with the updated player position
        screen.fill(WHITE)
        draw_board()
        draw_player(player_position)
        draw_button()
        
        # Update the display
        pygame.display.flip()
        # clock.tick(10)  # Control the speed of the animation (10 frames per second)
        # Add a small delay for smooth animation
        time.sleep(0.2)  # Pause for 0.2 seconds between steps

# Trigger event
def trigger_event(position):
    global player_money
    block = board[position]
    if block == "Chance" or block == "Chance 2":
        print("You landed on Chance! Drawing a card...")
    elif block == "Tax":
        player_money -= 100
        print("You paid $100 tax. Remaining money:", player_money)
    elif "Property" in block:
        print(f"You landed on {block}! You can buy it or pay rent.")
    elif block == "Go to Jail":
        print("You go to Jail! Miss a turn.")
    else:
        print(f"You are on {block}. Nothing happens.")

# Game loop
running = True
while running:
    screen.fill(WHITE)
    draw_board()
    draw_player(player_position)
    button_rect = draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos): 
                steps = roll_dice()
                print(f"You rolled a {steps}!")
                
                # Animate the player's movement
                animate_player_movement(player_position, steps)
                
                # Trigger the event at the final position
                trigger_event(player_position)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()