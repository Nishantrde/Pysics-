import pygame
import sys
import math
import cv2
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 720, 1280

# width, height = 920, 1020
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hollow Circle')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAROON = (128, 0, 0)

bindings_main = [((60,121), GREEN), ((120,181), RED), ((180,241), YELLOW)]

# Circle parameters
center = (width // 2, height // 4)
center2 = (width // 2, 2*height // 3)
radius = 200
thickness = 2  # Adjust this to change the thickness of the circle

# Set up the clock for FPS control
clock = pygame.time.Clock()

# Speed control variables
angle_degrees = 0
angle_speed = 1  # Change this to control the speed of rotation (1 for slow, higher for fast)

# Font for displaying voltage
font = pygame.font.SysFont(None, 36)

def simulate_voltage(angle):
    """ Simulates voltage based on the angle of the green sine wave. """
    # Voltage oscillates between -12 and 12
    voltage = 12 * math.sin(math.radians(angle))
    return voltage

fps = 60

# # OpenCV setup
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
# out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

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
    pygame.draw.line(screen, WHITE, (0, 2*height // 3), (width, 2*height // 3), 1)

    # Half-Cyan and Half-Maroon Magnet
    magnet_width, magnet_height = 50, 200  # Change the height to make the magnet taller
    magnet_surface = pygame.Surface((magnet_width, magnet_height), pygame.SRCALPHA)
    pygame.draw.rect(magnet_surface, CYAN, (0, 0, magnet_width, magnet_height // 2))  # Top half
    pygame.draw.rect(magnet_surface, MAROON, (0, magnet_height // 2, magnet_width, magnet_height // 2))  # Bottom half
    rotated_surface = pygame.transform.rotate(magnet_surface, angle_degrees + 90)
    rotated_rect = rotated_surface.get_rect(center=(center[0], center[1]))
    screen.blit(rotated_surface, rotated_rect.topleft)

    
    for bind in bindings_main:
        pos = bind[0]
        prv = None
        prv_oop = None
        bend = 20
        for i in range(pos[0], pos[1], 2):

            x = center[0] + (radius + bend) * math.cos(math.radians(i))
            y = center[1] - (radius + bend) * math.sin(math.radians(i))
            crr = (x,y)
            x = center[0] + (radius + bend) * math.cos(math.radians(i)+math.pi)
            y = center[1] - (radius + bend) * math.sin(math.radians(i)+math.pi)
            crr_oop = (x,y)
            if prv != None:
                pygame.draw.line(screen, bind[1], prv, crr, thickness)
            if prv_oop != None:
                pygame.draw.line(screen, bind[1], prv_oop, crr_oop, thickness)
            bend = -20 if bend == 20 else 20
            prv = crr
            prv_oop = crr_oop
        prv = None
        prv_oop = None

    # Simulate voltage and display it
    voltage1 = simulate_voltage(angle_degrees)  # Voltage tied to the green sine wave
    voltage2 = simulate_voltage(angle_degrees + 120)
    voltage3 = simulate_voltage(angle_degrees + 240)

    voltage_text1 = font.render(f"Voltage: {voltage1:.2f} V", True, GREEN)
    voltage_text2 = font.render(f"Voltage: {voltage2:.2f} V", True, RED)
    voltage_text3 = font.render(f"Voltage: {voltage3:.2f} V", True, YELLOW)


    screen.blit(voltage_text1, (60, (height //2)-15))  # Display voltage at the bottom left
    screen.blit(voltage_text2, (20 + 248, (height //2)-15))  # Display voltage at the bottom left
    screen.blit(voltage_text3, (20 + 460, (height //2)-15))  # Display voltage at the bottom left

    # Draw green, yellow, and red sine waves
    previous_point, previous_point2, previous_point3 = None, None, None
    ad = angle_degrees
    ad2 = ad + 240
    ad3 = ad2 + 240

    for x in range(center[0], width):
        ar = math.radians(ad)
        ar2 = math.radians(ad2)
        ar3 = math.radians(ad3)
        y = center2[1] - int(radius * math.sin(ar))
        y2 = center2[1] - int(radius * math.sin(ar2))
        y3 = center2[1] - int(radius * math.sin(ar3))
        current_point, current_point2, current_point3 = (x, y), (x, y2), (x, y3)
        if 0 <= y <= height and 0 <= y2 <= height and 0 <= y3 <= height:
            if previous_point:
                pygame.draw.line(screen, GREEN, previous_point, current_point, 2)
            if previous_point2:
                pygame.draw.line(screen, YELLOW, previous_point2, current_point2, 2)
            if previous_point3:
                pygame.draw.line(screen, RED, previous_point3, current_point3, 2)
        previous_point, previous_point2, previous_point3 = current_point, current_point2, current_point3
        ad += angle_speed
        ad2 += angle_speed
        ad3 += angle_speed

        if ad >= 360:
            ad -= 360
        if ad2 >= 360:
            ad2 -= 360
        if ad3 >= 360:
            ad3 -= 360
    
    # Draw green, yellow, and red sine waves
    previous_point, previous_point2, previous_point3 = None, None, None
    ad = angle_degrees
    ad2 = ad + 240
    ad3 = ad2 + 240

    for x in range(0, center[0]):
        ar = math.radians(ad)
        ar2 = math.radians(ad2)
        ar3 = math.radians(ad3)
        y = center2[1] - int(radius * math.sin(ar))
        y2 = center2[1] - int(radius * math.sin(ar2))
        y3 = center2[1] - int(radius * math.sin(ar3))
        current_point, current_point2, current_point3 = (x, y), (x, y2), (x, y3)
        if 0 <= y <= height and 0 <= y2 <= height and 0 <= y3 <= height:
            if previous_point:
                pygame.draw.line(screen, GREEN, previous_point, current_point, 2)
            if previous_point2:
                pygame.draw.line(screen, YELLOW, previous_point2, current_point2, 2)
            if previous_point3:
                pygame.draw.line(screen, RED, previous_point3, current_point3, 2)
        previous_point, previous_point2, previous_point3 = current_point, current_point2, current_point3
        ad += angle_speed
        ad2 += angle_speed
        ad3 += angle_speed

        if ad >= 360:
            ad -= 360
        if ad2 >= 360:
            ad2 -= 360
        if ad3 >= 360:
            ad3 -= 360


    angle_degrees += angle_speed
    if angle_degrees >= 360:
        angle_degrees = 0

    # # Capture the Pygame screen as a numpy array for OpenCV
    # frame = pygame.surfarray.array3d(screen)
    # frame = np.rot90(frame)  # Rotate the frame if needed
    # frame = np.flipud(frame)  # Flip the frame if needed
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR (for OpenCV)

    # # Write the frame to the video file
    # out.write(frame)

    # Update the display
    pygame.display.flip()
    clock.tick(fps)

# out.release()

pygame.quit()
sys.exit()
