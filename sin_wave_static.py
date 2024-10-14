import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 720, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sine Wave Graph')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRID_COLOR = (200, 200, 200)

# Circle parameters
center_y = height // 2  # Center along the y-axis for sine wave
amplitude = 100  # Amplitude of the sine wave (height of wave)
frequency = 0.02  # Frequency of the sine wave (controls the wave length)
speed = 4  # Speed of the wave movement
x_offset = 0  # Initial x offset

# Set up the clock for FPS control
clock = pygame.time.Clock()

# Function to draw gridlines
def draw_grid():
    # Draw vertical lines
    for x in range(0, width, 40):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, height), 1)

    # Draw horizontal lines
    for y in range(0, height, 40):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (width, y), 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the gridlines
    draw_grid()

    # Draw the x-axis and y-axis
    pygame.draw.line(screen, BLACK, (0, center_y), (width, center_y), 2)  # X-axis
    pygame.draw.line(screen, BLACK, (width // 2, 0), (width // 2, height), 2)  # Y-axis

    # Plot the sine wave by drawing connected lines between points
    previous_point = None
    for x in range(width//2, width):
        y = center_y + int(amplitude * math.sin(frequency * x))
        current_point = (x, y)
        print(y)

        if previous_point:
            pygame.draw.line(screen, RED, previous_point, current_point, 2)

        previous_point = current_point

   
    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 frames per second)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
