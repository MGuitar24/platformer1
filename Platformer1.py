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
from modules.physics import *
 
"""
Global constants
"""
 
# Colors
BLACK = (0,   0,   0)
 
# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600


 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Between the world of Black and Blue')

IMAGESDICT = {'player': pygame.image.load('player.png')}
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_manager = WallManager.WallManager(SCREEN_WIDTH, SCREEN_HEIGHT)
wall_list = wall_manager.get_walls()
all_sprite_list.add(wall_list)
 
# Create the player paddle object
player = Player.Player(50, 50, IMAGESDICT['player'])
player.walls = wall_list
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False

eventsManager = EventsManager.EventsManager(player)

while not done:
	for event in pygame.event.get():
		done = eventsManager.determineEvent(event)
	PhysicsEngine.PhysicsEngine().applyGravity(player)
	all_sprite_list.update()
	screen.fill(BLACK)
	all_sprite_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()