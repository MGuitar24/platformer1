import pygame
from modules.resource_handling.images import *

class Background(pygame.sprite.Sprite):
    iWidth = 100
    iHeight = 81
    
    def __init__(self, spriteSheet):
        spriteMap = Spritesheet.Spritesheet(spriteSheet)
        spritesheetUtility = SpritesheetUtility.SpritesheetUtility()
        self.image = spriteMap.image_at((2, 2, self.iWidth, self.iHeight), colorkey=spritesheetUtility.WHITE)
        self.rect = self.image.get_rect()