import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WW2 Game")
clock = pygame.time.Clock()

pygame.mixer.music.load("wwii_theme.mp3")
pygame.mixer.music.play(-1)  # Loop the music

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Board and player setup
board = [
    "Start", "Battle of Stalingrad", "Chance", "D-Day", "War Tax", 
    "Pearl Harbor", "Go to POW Camp", "Free Supplies", "Chance 2", 
    "Battle of Midway", "Berlin", "Allied Aid", "Luxury Tax", 
    "Aircraft Carrier", "Supply Depot", "Battle of Britain"
]


block_positions = [(100 + i * 100, 500) for i in range(4)] + \
                  [(500, 500 - i * 100) for i in range(4)] + \
                  [(500 - i * 100, 100) for i in range(4)] + \
                  [(100, 100 + i * 100) for i in range(4)]

player_position = 0
player_resources = 1500
player_icon = pygame.image.load("tank_icon.png")
player_icon = pygame.transform.scale(player_icon, (40, 40))

player_roles = ["Allied Forces", "Axis Powers"]
player_role = random.choice(player_roles)
print(f"You are playing as: {player_role}")

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
        print("You encountered a war event! Drawing a card...")
        # Add random events here
    elif block == "War Tax":
        player_money -= 200
        print("You paid $200 for war supplies. Remaining money:", player_money)
    elif "Battle" in block:
        print(f"You landed on {block}! Prepare for battle!")
        battle()
    elif block == "Go to POW Camp":
        print("You are captured! Go to POW Camp and miss a turn.")
    else:
        print(f"You are at {block}. Nothing happens.")
        
def battle():
    print("A battle begins!")
    player_roll = roll_dice()
    enemy_roll = roll_dice()
    if player_roll > enemy_roll:
        print("You won the battle! Gain 100 resources.")
        global player_resources
        player_resources += 100
    else:
        print("You lost the battle! Lose 100 resources.")
        player_resources -= 100

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