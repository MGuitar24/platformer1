"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example
 
Explanation video: http://youtu.be/8IRyt7ft7zg
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
 
import pygame

from modules.sprites import *
from modules.events import *
 
"""
Global constants
"""
 
# Colors
BLACK    = (   0,   0,   0)
 
# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Between the world of Black and Blue')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
#Left Side wall
wall = Wall.Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

#Top wall
wall = Wall.Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#Small ledge
wall = Wall.Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#Right Side Wall
wall = Wall.Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall.Wall(0, 590, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
# Create the player paddle object
player = Player.Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)

# Create the player paddle object
#player2 = Player.Player(70, 50)
#player2.walls = wall_list
#all_sprite_list.add(player2)
 
clock = pygame.time.Clock()
 
done = False

eventsManager = EventsManager.EventsManager(player)
#eventsManager2 = EventsManager.EventsManager(player2)

while not done:
 
    for event in pygame.event.get():
        done = eventsManager.determineEvent(event)
#        eventsManager2.determineEvent(event)
 
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()