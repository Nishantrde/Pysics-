import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 720, 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hollow Circle')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (25, 150, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 100, 0)

# Circle parameters
center = (width // 2, height // 2)
radius = 200
thickness = 2

# Set up the clock for FPS control
clock = pygame.time.Clock()

# Speed control variables
angle_degrees = 0
angle_speed = 1

font = pygame.font.SysFont(None, 48)  # Default system font, size 48
line_font = pygame.font.SysFont(None, 30)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the hollow circle
    pygame.draw.circle(screen, WHITE, center, radius, thickness)

    # Draw the vertical and horizontal axes
    pygame.draw.line(screen, WHITE, (width // 2, 0), (width // 2, height), 1)
    pygame.draw.line(screen, WHITE, (0, height // 2), (width, height // 2), 1)

    # Calculate endpoint of the radius line
    angle_radians = math.radians(angle_degrees)
    end_x = center[0] + int(radius * math.cos(angle_radians))
    end_y = center[1] - int(radius * math.sin(angle_radians))

    # Draw the red radius line
    pygame.draw.line(screen, RED, center, (end_x, end_y), 3)

    # Calculate and display the trigonometric values
    sin_value = round(math.sin(angle_radians), 2)
    cos_value = round(math.cos(angle_radians), 2)
    tan_value = "Undefined" if cos_value == 0 else round(math.tan(angle_radians), 2)

    # Render and display the text
    sin_text = font.render(f'sin({angle_degrees}) = {sin_value}', True, GREEN)
    cos_text = font.render(f'cos({angle_degrees}) = {cos_value}', True, PURPLE)
    tan_text = font.render(f'tan({angle_degrees}) = {tan_value}', True, YELLOW)

    # Position the text
    sin_text_rect = sin_text.get_rect(center=(width // 3, height // 3 - 250))
    cos_text_rect = cos_text.get_rect(center=(width // 3, height // 3 - 200))
    tan_text_rect = tan_text.get_rect(center=(width // 3, height // 3 - 150))

    # Blit the text on the screen
    screen.blit(sin_text, sin_text_rect)
    screen.blit(cos_text, cos_text_rect)
    screen.blit(tan_text, tan_text_rect)

    # Draw additional trigonometric lines
    pygame.draw.line(screen, GREEN, (end_x, end_y), (end_x, center[1]), 3)
    pygame.draw.line(screen, CYAN, center, (center[0] + radius * (1 / math.cos(angle_radians)), center[1]), 3)
    pygame.draw.line(screen, PURPLE, (center[0], end_y), (end_x, end_y), 3)
    pygame.draw.line(screen, YELLOW, (end_x, end_y), (center[0] + radius * (1 / math.cos(angle_radians)), center[1]), 3)

    if math.sin(angle_radians) != 0:
        pygame.draw.line(screen, BLUE, (end_x, end_y), (center[0], center[1] - radius * (1 / math.sin(angle_radians))), 3)
        pygame.draw.line(screen, ORANGE, center, (center[0], center[1] - radius * (1 / math.sin(angle_radians))), 3)

    # Draw the angle arc
    arc_radius = 50
    arc_rect = pygame.Rect(center[0] - arc_radius, center[1] - arc_radius, 2 * arc_radius, 2 * arc_radius)
    pygame.draw.arc(screen, BLUE, arc_rect, 0, angle_radians, 3)

    # Display the angle in degrees
    angle_text = font.render(f'{int(angle_degrees)}°', True, WHITE)
    angle_pos = (center[0] + int(arc_radius * math.cos(angle_radians / 2)),
                 center[1] - int(arc_radius * math.sin(angle_radians / 2)))
    screen.blit(angle_text, angle_pos)

    # Increment the angle
    angle_degrees += angle_speed
    if angle_degrees >= 360:
        angle_degrees = 0

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

pygame.quit()
sys.exit()
