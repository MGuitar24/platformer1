import pygame
from pygame import *

class Camera(object):
    def __init__(self, camera_func, width, height):
    	#print "Camera created"
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
    	#print self.state.topleft
        return target.rect.move(self.state.topleft)

    def update(self, target):
    	#print target.rect
        self.state = self.camera_func(self.state, target.rect)