import pygame
from modules.resource_handling.images import *

class Chest(pygame.sprite.Sprite):

	chestAnimation = []
	iWidth = 35
	iHeight = 34

	def __init__(self, x, y, spriteSheet):
		pygame.sprite.Sprite.__init__(self)
		spriteMap = Spritesheet.Spritesheet(spriteSheet)
		spritesheetUtility = SpritesheetUtility.SpritesheetUtility()
		self.chestAnimation.append(spriteMap.image_at((0, 0, self.iWidth, self.iHeight), colorkey=spritesheetUtility.WHITE))
		self.chestAnimation.append(spriteMap.image_at((self.iWidth, 0, self.iWidth, self.iHeight), colorkey=spritesheetUtility.WHITE))

		self.image = self.chestAnimation[0]

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x