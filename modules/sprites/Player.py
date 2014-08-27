import pygame
from modules.resource_handling.images import *

WHITE    = ( 255, 255, 255)

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
 
    # Set speed vector
    change_x = 0
    change_y = 0
    animationSwitchThreshold = 9
    animationSwitchCount = 0
    animationFrames = 9
    currentFrame = 0
    direction = 1
    moving = False
    walls = None
    velocity = 6
    max_gravity = 10
    max_parachute_speed = 1
    max_fall_speed = max_gravity
    jumping = False
    jumpingTwice = False
    iWidth = 28                 # The width of the sprite
    iHeight = 46                # The height of the sprite
    imageLeftY = 79             # Left animation y value
    imageDownY = 143            # Down animation y value
    imageRightY = 207           # Right animation y value
    downAnimationFrames = []
    rightAnimationFrames = []
    leftAnimationFrames = []
        
    # Constructor function
    def __init__(self, playerSpriteSheet):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        spriteMap = Spritesheet.Spritesheet(playerSpriteSheet)
        spritesheetUtility = SpritesheetUtility.SpritesheetUtility()
        self.downAnimationFrames = spritesheetUtility.animationFramesLoader(18, self.imageDownY, self.iWidth, self.iHeight, 64, spriteMap)
        self.rightAnimationFrames = spritesheetUtility.animationFramesLoader(18, self.imageRightY, self.iWidth, self.iHeight, 64,  spriteMap)
        self.leftAnimationFrames = spritesheetUtility.animationFramesLoader(18, self.imageLeftY, self.iWidth, self.iHeight, 64, spriteMap)
        
        self.image = self.downAnimationFrames[self.currentFrame]
 
        self.rect = self.image.get_rect()
 
    def change_location(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x):
        """ Change the speed of the player. """
        self.change_x += x * self.velocity

    def applyGravity(self):
        if self.change_y < self.max_fall_speed:
            self.change_y += 1
        elif self.change_y > self.max_fall_speed:
            self.change_y = self.max_fall_speed
 
    def jump(self):
        if self.jumping and not self.jumpingTwice:
            self.change_y = -16
            self.jumpingTwice = True
        if not self.jumping:
            self.change_y = -16
            self.jumping = True

    def deploy_parachute(self):
        self.max_fall_speed = self.max_parachute_speed

    def undeploy_parachute(self):
        self.max_fall_speed = self.max_gravity

    def determine_animation_for_direction(self):
        if self.direction == 3:
            return self.leftAnimationFrames
        else:
            return self.rightAnimationFrames

    def update_animation(self):
        if self.moving:
            if self.animationSwitchCount == self.animationSwitchThreshold:
                self.image = self.determine_animation_for_direction()[self.currentFrame]
                self.currentFrame += 1
                if self.currentFrame > 8:
                    self.currentFrame = 0
                self.animationSwitchCount = 0
            else:
                self.animationSwitchCount += 1

    def update(self):
        self.update_animation()

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
                self.jumpingTwice = False
                self.change_y = 0
            else:
                self.rect.top = block.rect.bottom
                self.jumping = False
                self.jumpingTwice = False
                self.change_y = 0
