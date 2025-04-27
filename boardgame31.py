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

background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
screen.blit(background, (0, 0))

# Uncomment the following lines if "wwii_theme.mp3" exists in the same directory.
# pygame.mixer.music.load("wwii_theme.mp3")
# pygame.mixer.music.play(-1)  # Loop the music

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

# Players setup
players = [
    {"name": "Player", "position": 0, "resources": 1500, "is_pc": False},
    {"name": "PC", "position": 0, "resources": 1500, "is_pc": True}
]
current_player = 0

# Properties setup
properties = {
    "Battle of Stalingrad": {"owner": None, "cost": 200, "rent": 50},
    "D-Day": {"owner": None, "cost": 300, "rent": 75},
    "Pearl Harbor": {"owner": None, "cost": 250, "rent": 60},
    "Battle of Midway": {"owner": None, "cost": 350, "rent": 90},
    "Berlin": {"owner": None, "cost": 400, "rent": 100},
    "Aircraft Carrier": {"owner": None, "cost": 500, "rent": 120},
    "Supply Depot": {"owner": None, "cost": 150, "rent": 40},
    "Battle of Britain": {"owner": None, "cost": 450, "rent": 110}
}

# Chance cards
chance_cards = [
    "Gain 200 resources.",
    "Lose 100 resources.",
    "Move forward 3 spaces.",
    "Go to POW Camp."
]

# Dice function
def roll_dice():
    return random.randint(1, 6)

# Draw the board
def draw_board():
    for i, pos in enumerate(block_positions):
        pygame.draw.rect(screen, BLUE if i % 2 == 0 else GREEN, (*pos, 80, 80), border_radius=10)
        pygame.draw.rect(screen, BLACK, (*pos, 80, 80), 2)  # Add a black border
        font = pygame.font.Font(None, 12)
        text = font.render(board[i], True, WHITE)
        screen.blit(text, (pos[0] + 5, pos[1] + 5))
        
        # Check if the block is owned
        if board[i] in properties and properties[board[i]]["owner"] is not None:
            owner_index = properties[board[i]]["owner"]
            owner_color = RED if owner_index == 0 else BLACK  # Player 1 = RED, PC = BLACK
            
            # Draw a small circle to indicate ownership
            pygame.draw.circle(screen, owner_color, (pos[0] + 70, pos[1] + 10), 8)

# Draw the player
player_icons = [
    pygame.image.load("images/player_icon1.png"),
    pygame.image.load("images/player_icon2.png")
]
player_icons = [pygame.transform.scale(icon, (40, 40)) for icon in player_icons]

def draw_player(position, player_index):
    x, y = block_positions[position]
    screen.blit(player_icons[player_index], (x + 20, y + 20))
    
def draw_active_player():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Turn: {players[current_player]['name']}", True, RED)
    screen.blit(text, (10, 10))
    
def draw_button():
    button_rect = pygame.Rect(WIDTH - 200, HEIGHT - 100, 100, 50)
    pygame.draw.rect(screen, RED, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Roll Dice", True, WHITE)
    screen.blit(text, (button_rect.x + 10, button_rect.y + 10))
    return button_rect

def roll_dice_animation():
    for _ in range(10):  # Simulate dice rolling
        dice_value = random.randint(1, 6)
        dice_image = pygame.image.load(f"images/dice_{dice_value}.png")
        dice_image = pygame.transform.scale(dice_image, (50, 50))
        screen.blit(dice_image, (WIDTH // 2 - 25, HEIGHT // 2 - 25))
        pygame.display.flip()
        time.sleep(0.1)
    return dice_value

# Function to animate player movement
def animate_player_movement(start_position, steps, player_index):
    for step in range(1, steps + 1):
        players[player_index]["position"] = (start_position + step) % len(board)
        screen.fill(WHITE)
        draw_board()
        for i, player in enumerate(players):
            draw_player(player["position"], i)
        draw_button()
        pygame.display.flip()
        time.sleep(0.2)

def animate_ownership(block_index, owner_index):
    pos = block_positions[block_index]
    owner_color = RED if owner_index == 0 else BLACK
    for size in range(2, 10):
        pygame.draw.circle(screen, owner_color, (pos[0] + 70, pos[1] + 10), size)
        pygame.display.flip()
        time.sleep(0.05)

def fade_in():
    for alpha in range(0, 255, 5):
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(alpha)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        time.sleep(0.05)
        
def draw_hud():
    font = pygame.font.Font(None, 24)
    for i, player in enumerate(players):
        text = font.render(f"{player['name']}: {player['resources']} resources", True, RED if i == 0 else BLACK)
        screen.blit(text, (10, 50 + i * 30))

def draw_tooltip(text, pos):
    font = pygame.font.Font(None, 20)
    tooltip = font.render(text, True, WHITE)
    screen.blit(tooltip, (pos[0] + 10, pos[1] - 20))

def show_victory_screen(winner):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 72)
    text = font.render(f"{winner['name']} Wins!", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)
    
# Trigger event
def trigger_event(position, player_index):
    block = board[position]
    player = players[player_index]

    if block == "Chance" or block == "Chance 2":
        card = random.choice(chance_cards)
        print(f"{player['name']} drew a Chance card: {card}")
        if "Gain" in card:
            player["resources"] += 200
        elif "Lose" in card:
            player["resources"] -= 100
        elif "Move forward" in card:
            animate_player_movement(player["position"], 3, player_index)
        elif "POW Camp" in card:
            player["position"] = board.index("Go to POW Camp")
    elif block == "War Tax":
        player["resources"] -= 200
        print(f"{player['name']} paid 200 resources for war supplies.")
    elif block in properties:
        property = properties[block]
        if property["owner"] is None:
            if player["resources"] >= property["cost"]:
                if not player["is_pc"]:  # Player decision
                    print(f"{block} is unowned. You can buy it for {property['cost']} resources.")
                    player["resources"] -= property["cost"]
                    property["owner"] = player_index
                else:  # PC decision
                    player["resources"] -= property["cost"]
                    property["owner"] = player_index
                    print(f"{player['name']} bought {block} for {property['cost']} resources.")
        elif property["owner"] != player_index:
            rent = property["rent"]
            print(f"{block} is owned by another player. {player['name']} paid {rent} resources as rent.")
            player["resources"] -= rent
            players[property["owner"]]["resources"] += rent
    elif block == "Go to POW Camp":
        print(f"{player['name']} is captured! Go to POW Camp and miss a turn.")
        player["position"] = board.index("Go to POW Camp")
    else:
        print(f"{player['name']} is at {block}. Nothing happens.")

# Check victory condition
def check_victory():
    for player in players:
        if player["resources"] >= 5000:
            print(f"{player['name']} wins the game!")
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))  # Add background
    draw_board()
    draw_hud()
    draw_active_player()
    for i, player in enumerate(players):
        draw_player(player["position"], i)
    button_rect = draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not players[current_player]["is_pc"]:
            if button_rect.collidepoint(event.pos): 
                steps = roll_dice()
                print(f"{players[current_player]['name']} rolled a {steps}!")
                animate_player_movement(players[current_player]["position"], steps, current_player)
                #players[current_player]["position"] = (players[current_player]["position"] + steps) % len(board)
                trigger_event(players[current_player]["position"], current_player)
                if check_victory():
                    running = False
                current_player = (current_player + 1) % len(players)

    # PC Turn
    if players[current_player]["is_pc"] and running:
        time.sleep(1)  # Delay for PC turn
        steps = roll_dice()
        print(f"{players[current_player]['name']} rolled a {steps}!")
        animate_player_movement(players[current_player]["position"], steps, current_player)
        #players[current_player]["position"] = (players[current_player]["position"] + steps) % len(board)
        trigger_event(players[current_player]["position"], current_player)
        if check_victory():
            running = False
        current_player = (current_player + 1) % len(players)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()