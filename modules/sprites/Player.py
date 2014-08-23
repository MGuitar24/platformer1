import pygame

WHITE    = ( 255, 255, 255)

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
 
    # Set speed vector
    change_x = 0
    change_y = 0
    walls = None
    velocity = 6
    max_gravity = 10
    jumping = False
 
    # Constructor function
    def __init__(self, x, y, spriteImage):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = spriteImage
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x):
        """ Change the speed of the player. """
        self.change_x += x * self.velocity

    def applyGravity(self):
        if self.change_y < self.max_gravity:
            self.change_y += 1
 
    def jump(self):
        if not self.jumping:
            self.change_y = -16
            self.jumping = True

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.jumping = False
            else:
                self.rect.top = block.rect.bottom