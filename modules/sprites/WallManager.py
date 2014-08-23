""" Manages the levels """
import pygame
from modules.sprites import Wall

class WallManager:
	def get_walls(self):
		wall_list = pygame.sprite.Group()

		#Left Side wall
		wall = Wall.Wall(0, 0, 10, 600)
		wall_list.add(wall)

		#Top wall
		wall = Wall.Wall(10, 0, 790, 10)
		wall_list.add(wall)

		#Small ledge
		wall = Wall.Wall(10, 200, 100, 10)
		wall_list.add(wall)

		#Right Side Wall
		wall = Wall.Wall(790, 0, 10, 600)
		wall_list.add(wall)

		wall = Wall.Wall(0, 590, 800, 10)
		wall_list.add(wall)

		return wall_list