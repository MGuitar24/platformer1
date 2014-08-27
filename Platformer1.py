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
from pygame import *
 
"""
Global constants
"""
 
# Colors
BLACK = (0,   0,   0)
PINK = (255, 20, 147)

properties = dict(line.strip().split('=') for line in open('settings.ini'))

resourceFiles = {}
resourceFiles["MAIN_CHARACTER"] = 'resources/spritemaps/BODY_skeleton.png'

HALF_WIDTH = int(int(properties['SCREEN_WIDTH']) / 2)
HALF_HEIGHT = int(int(properties['SCREEN_HEIGHT']) / 2)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-int(properties['SCREEN_WIDTH'])), l)   # stop scrolling at the right edge
    t = max(-(camera.height-int(properties['SCREEN_HEIGHT'])), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)
    
# Call this function so the Pygame library can initialize itself
pygame.init()

screen = pygame.display.set_mode([int(properties['SCREEN_WIDTH']), int(properties['SCREEN_HEIGHT'])])

# Set the title of the window
pygame.display.set_caption('Between the world of Black and Blue')
all_sprite_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
all_proximity_entities_list = []
background = Background.Background()

level_manager = LevelManager.LevelManager(all_sprite_group, wall_group, all_proximity_entities_list, background)
level_manager.load_level(1)

# Create the player paddle object
playerSpriteSheet = resourceFiles["MAIN_CHARACTER"]
player = Player.Player(50, 50, playerSpriteSheet)
player.walls = wall_group
all_sprite_group.add(player)
 
clock = pygame.time.Clock()
 
done = False    

camera = Camera.Camera(complex_camera, int(properties['LEVEL_WIDTH']), int(properties['LEVEL_HEIGHT']))

eventsManager = EventsManager.EventsManager(player)
proximityManager = ProximityManager.ProximityManager((player,))

while not done:
    for event in pygame.event.get():
        done = eventsManager.determineEvent(event)
    PhysicsEngine.PhysicsEngine().applyGravity([player])
    all_sprite_group.update()
    screen.fill(PINK)
    camera.update(player)
    proximityManager.checkProximityToPlayers(all_proximity_entities_list)
    for y in range(0, int(properties['LEVEL_HEIGHT']), background.iHeight):
        for x in range(0, int(properties['LEVEL_WIDTH']), background.iWidth):
            background.rect.x = x
            background.rect.y = y
            screen.blit( background.image,camera.apply(background))
    for entity in all_sprite_group:
            screen.blit(entity.image, camera.apply(entity))
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
