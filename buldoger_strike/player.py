from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game  = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        
        # Forward / Backward movement (W/S)
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        
        # Left / Right movement (A/D)
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # Check collision before updating position
        self.check_wall_collision(dx, dy)

        # Rotational movement (Left/Right arrow keys)
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        # Keep angle in the range [0, 2π]
        self.angle %= math.tau

    def check_wall(self, x, y):
        """Check if the player is trying to move into a wall."""
        return (int(x), int(y)) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        """Prevent player from passing through walls."""
        if self.check_wall(self.x + dx, self.y):
            self.x += dx
        if self.check_wall(self.x, self.y + dy):
            self.y += dy

    def draw(self):
        """Draw player and the direction they're facing."""
        # Scaling factor for drawing
        scale_factor = 2  # Half the screen
        size_x = int(WIDTH / len(mini_map[0]))  # Width of each grid block
        size_y = int(HEIGHT / len(mini_map) / scale_factor)  # Height of each grid block
        
        # pg.draw.line(self.game.screen, 'yellow', 
        #              (self.x * size_x, self.y * size_y),
        #              (self.x * size_x + WIDTH * math.cos(self.angle), 
        #               self.y * size_y + WIDTH * math.sin(self.angle)), 2)

        # Calculate the end point of the line
        line_end_x = self.x * size_x + 500 * math.cos(self.angle)
        line_end_y = HEIGHT//2 if self.y * size_y + 500 * math.sin(self.angle) > HEIGHT//2 else self.y * size_y + 500 * math.sin(self.angle)
        line_end_y = HEIGHT//2 if line_end_y > HEIGHT//2 else line_end_y
        
        pg.draw.line(self.game.screen, 'yellow', 
                     (self.x * size_x, self.y * size_y),
                     (line_end_x, line_end_y), 2)

        pg.draw.circle(self.game.screen, 'green', 
                       (self.x * size_x, self.y * size_y), 15)
        
        pg.draw.circle(self.game.screen, 'green', 
                       (WIDTH//2, 2*HEIGHT//3 ), 15)

        line_length = math.sqrt(2*10000) # Diagonal length of the square

        pg.draw.circle(self.game.screen, 'white', (WIDTH//2, 2*HEIGHT//3 ), line_length, 3)
        
        # angle_offset = math.radians(45)  # Convert 45 degrees to radians

        pg.draw.line(self.game.screen, 'white', 
            (WIDTH//2 + int(line_length * math.cos(math.radians(0))), 
            2*HEIGHT//3 + int(line_length * math.sin(math.radians(0)))), 
            (WIDTH//2 + int(line_length * math.cos(math.pi)), 
            2*HEIGHT//3 + int(line_length * math.sin(math.pi))), 2)

        pg.draw.line(self.game.screen, 'white', 
            (WIDTH//2 - int(line_length * math.cos(math.radians(90))), 
            2*HEIGHT//3 - int(line_length * math.sin(math.radians(90)))), 
            (WIDTH//2 - int(line_length * math.cos(math.radians(270))), 
            2*HEIGHT//3 - int(line_length * math.sin(math.radians(270)))), 2)
        
        # Length of the diagonal line (sqrt(2) * side length of 100)
        line_length = math.sqrt(2*10000) # Diagonal length of the square

        # Calculate the end point of the yellow line (aligned with the player's facing direction)
        line_end_x = WIDTH // 2 + int(line_length * math.cos(self.angle))
        line_end_y = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle))
        line_end_x_opp = WIDTH // 2 + int(line_length * math.cos(self.angle+math.pi))
        line_end_y_opp = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle+math.pi))

        line_end_x_opp_90 = WIDTH // 2 + int(line_length * math.cos(self.angle+math.radians(270)))
        line_end_y_opp_90 = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle+math.radians(270)))

        line_end_x_90 = WIDTH // 2 + int(line_length * math.cos(self.angle+math.radians(90)))
        line_end_y_90 = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle+math.radians(90)))

        # Draw the diagonal yellow line from the center of the square
        pg.draw.line(self.game.screen, 'yellow', 
                    (line_end_x_opp, line_end_y_opp), 
                    (line_end_x, line_end_y), 2)
        
        pg.draw.line(self.game.screen, 'yellow', 
                    (line_end_x_90, line_end_y_90), 
                    (line_end_x_opp_90, line_end_y_opp_90), 2)
        
        pg.draw.line(self.game.screen, 'red',  
            (line_end_x, 2 * HEIGHT // 3),
            (line_end_x, line_end_y), 3)
        
        pg.draw.line(self.game.screen, 'blue', 
            (WIDTH // 2, line_end_y),
            (line_end_x, line_end_y), 3)

        center_x, center_y = WIDTH // 2, 2 * HEIGHT // 3

        # Step 1: Calculate the angle between the yellow line and the X-axis
        dy = -(line_end_y - center_y)  # Invert the dy value to account for Pygame's inverted Y-axis
        dx = line_end_x - center_x
        angle_with_x_axis = math.degrees(math.atan2(dy, dx))  # Convert radians to degrees

        # Ensure the angle is positive
        if angle_with_x_axis < 0:
            angle_with_x_axis += 360

        # Step 2: Draw the arc for the angle
        arc_rect = pg.Rect(center_x - 50, center_y - 50, 100, 100)  # Rectangle for arc
        pg.draw.arc(self.game.screen, 'white', arc_rect, 0, math.radians(angle_with_x_axis), 2)

        # Step 3: Display the angle value as text
        font = pg.font.Font(None, 36)
        angle_text = font.render(f'Angle: {int(angle_with_x_axis)}°', True, (255, 100, 25))
        self.game.screen.blit(angle_text, (line_end_x, line_end_y-30))  # Positioning text

        keys = pg.key.get_pressed()
        pos = (line_end_x, line_end_y)
        if keys[pg.K_w]:
            line_end_x = WIDTH // 2 + int(line_length * math.cos(self.angle))
            line_end_y = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle))
            pos = (line_end_x, line_end_y)
        
        if keys[pg.K_s]:
            line_end_x = WIDTH // 2 + int(line_length * math.cos(self.angle+math.pi))
            line_end_y = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle+math.pi))
            pos = (line_end_x, line_end_y)
        
        if keys[pg.K_a]:
            line_end_x = WIDTH // 2 + int(line_length * math.cos(self.angle+math.radians(90)))
            line_end_y = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle+math.radians(90)))
            pos = (line_end_x, line_end_y)
        
        if keys[pg.K_d]:
            line_end_x = WIDTH // 2 + int(line_length * math.cos(self.angle+math.radians(270)))
            line_end_y = 2 * HEIGHT // 3 + int(line_length * math.sin(self.angle+math.radians(270)))
            pos = (line_end_x, line_end_y)

        

        # Show which key is being pressed
        keys = pg.key.get_pressed()
        key_text = ''
        if keys[pg.K_w]:
            key_text = 'W'
        if keys[pg.K_s]:
            key_text = 'S'
        if keys[pg.K_a]:
            key_text = 'A'
        if keys[pg.K_d]:
            key_text = 'D'
        
        # Display the key pressed on the screen
        if key_text:
            key_display_text = font.render(f'Key Pressed: {key_text}', True, 'white')
            self.game.screen.blit(key_display_text, (center_x - 80, center_y + 170))  # Display at top left corner

        # Display player's (dx, dy) on the screen
        text_surface = font.render(f'(dx, dy): {int(self.x*size_x)}, {int(self.y*size_y)}', True, 'orange')
        self.game.screen.blit(text_surface, (line_end_x, line_end_y))
        

    def update(self):
        """Update player movement."""
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
