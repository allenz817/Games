import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Board Game")
running = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    # Draw a simple board
    for row in range(8):
        for col in range(8):
            color = RED if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * 75, row * 75, 75, 75))
    
    pygame.display.update()

pygame.quit()