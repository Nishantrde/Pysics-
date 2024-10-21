import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 400, 600
screen = pygame.display.set_mode((width, height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
DARK_GREY = (50, 50, 50)

# Function to draw coil-like zigzag
def draw_coil(screen, start_x, start_y, line_length, num_zigs, spacing, thickness):
    points = []
    
    # Generate the points for zigzag
    for i in range(num_zigs):
        # Alternate between upward and downward zigs
        if i % 2 == 0:
            x1 = start_x
            x2 = start_x + line_length
        else:
            x1 = start_x + line_length
            x2 = start_x
            
        y1 = start_y + i * spacing
        y2 = start_y + (i + 1) * spacing
        
        points.append((x1, y1))
        points.append((x2, y2))
        
        
        pygame.draw.line(screen, GREY, (x1, y1), (x2, y2), thickness)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Fill screen with white background
    
    # Draw the coil shape
    draw_coil(screen, 100, 50, 150, 12, 40, 4)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Cap the frame rate at 60 FPS

pygame.quit()
sys.exit()
