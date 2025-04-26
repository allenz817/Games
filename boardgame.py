        
import random


board = ["Start", "Property A", "Chance", "Property B", "Tax", "Property C", "Go to Jail", "Free Parking", "Chance 2", "Property D"]

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500  # Starting money
    
    def move(self, steps):
        self.position = (self.position + steps) % len(board)

def roll_dice():
    return random.randint(1, 6)

def trigger_event(player):
    current_block = board[player.position]
    if current_block == "Chance":
        print(f"{player.name} landed on Chance! Draw a card.")
    elif current_block == "Tax":
        player.money -= 100
        print(f"{player.name} paid $100 tax. Remaining money: ${player.money}")
    elif "Property" in current_block:
        print(f"{player.name} landed on {current_block}! You can buy or pay rent.")
    else:
        print(f"{player.name} is on {current_block}.")
        
def play_game():
    player = Player("Player 1")
    game_running = True
    
    while game_running:
        input("Press Enter to roll the dice...")
        steps = roll_dice()
        print(f"{player.name} rolled a {steps}.")
        player.move(steps)
        print(f"{player.name} moved to position {player.position} ({board[player.position]}).")
        trigger_event(player)
        
        # End game condition (example: player goes bankrupt)
        if player.money <= 0:
            print(f"{player.name} is bankrupt! Game over.")
            game_running = False

play_game()