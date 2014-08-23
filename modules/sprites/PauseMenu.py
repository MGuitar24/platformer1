import pygame
class PauseMenu(pygame.sprite.Sprite):
	def __init__(self, x, y, spriteImage):
		pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        #self.image = spriteImage
 
        # Make our top-left corner the passed-in location.
        #self.rect = self.image.get_rect()
        #self.rect.y = y
        #self.rect.x = x