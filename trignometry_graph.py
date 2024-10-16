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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Circle parameters
center = (width // 2, height // 2)
radius = 200
thickness = 2  # Adjust this to change the thickness of the circle

# Set up the clock for FPS control
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)  # Default system font, size 48
line_font = pygame.font.SysFont(None, 30)  # Font for radius text

# Speed control variables
angle_degrees = 0
angle_speed = 1  # Change this to control the speed of rotation (1 for slow, higher for fast)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, center, radius, thickness)
    pygame.draw.line(screen, WHITE, (width // 2, 0), (width // 2, height), 1)
    pygame.draw.line(screen, WHITE, (0, height // 2), (width, height // 2), 1)

    # Calculate endpoint of the line at current angle
    angle_radians = math.radians(angle_degrees)
    end_x = center[0] + int(radius * math.cos(angle_radians))
    end_y = center[1] - int(radius * math.sin(angle_radians))

    # Corrected radius text positioning
    radius_text = line_font.render('r', True, RED)
    radius_pos = radius_text.get_rect(center=((center[0] + end_x) // 2, ((center[1] + end_y) // 2) - 8))
    screen.blit(radius_text, radius_pos)

    # Drawing main circle lines
    pygame.draw.line(screen, RED, center, (end_x, end_y), 3)
    pygame.draw.line(screen, GREEN, (end_x, end_y), (end_x, center[1]), 3)
    pygame.draw.line(screen, CYAN, center, (center[0] + radius * (1 / math.cos(angle_radians)), center[1]), 3)
    pygame.draw.line(screen, MAGENTA, (center[0], end_y), (end_x, end_y), 3)
    pygame.draw.line(screen, YELLOW, (end_x, end_y), (center[0] + radius * (1 / math.cos(angle_radians)), center[1]), 3)

    if math.sin(angle_radians) != 0:
        pygame.draw.line(screen, BLUE, (end_x, end_y), (center[0], center[1] - radius * (1 / math.sin(angle_radians))), 3)
        pygame.draw.line(screen, ORANGE, center, (center[0], center[1] - radius * (1 / math.sin(angle_radians))), 3)

    # Increment the angle for the next frame
    angle_degrees += angle_speed
    if angle_degrees >= 360:
        angle_degrees = 0

    # Plot Sine, Cosine, and Tangent waves
    # Sine wave (magenta)
    previous_point = None
    ad = angle_degrees
    for y in range(center[1], height):
        ar = math.radians(ad)
        x = center[0] + int(radius * math.cos(ar))
        current_point = (x, y)

        if previous_point:
            pygame.draw.line(screen, MAGENTA, previous_point, current_point, 2)

        previous_point = current_point
        ad += angle_speed
        if ad > 360:
            ad = 0

    # Cosine wave (green)
    previous__point = None
    ad = angle_degrees
    for x in range(0, center[0]):
        ar = math.radians(ad)
        y = center[1] - int(radius * math.sin(ar))
        current__point = (x, y)

        if previous__point:
            pygame.draw.line(screen, GREEN, previous__point, current__point, 2)

        previous__point = current__point
        ad += angle_speed
        if ad > 360:
            ad = 0

    # Tangent wave (yellow) with out-of-bound protection
    ad = angle_degrees
    previous___point = None
    for x in range(center[0], width):
        ar = math.radians(ad)
        try:
            y = center[1] - int(radius * math.tan(ar))
            current___point = (x, y)

            if 0 <= y < height:
                if previous___point:
                    pygame.draw.line(screen, YELLOW, previous___point, current___point, 2)

        except (ValueError, OverflowError):
            pass
        previous___point = current___point
        ad += angle_speed
        if ad > 360:
            ad = 0

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

sys.exit()
