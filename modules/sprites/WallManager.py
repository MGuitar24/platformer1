""" Manages the levels """
import pygame
from modules.sprites import Wall

class WallManager:
	wall_properties = {'wall_thickness': 10, 'level_width': 1200}	
	wall_properties['right_wall_x_pos'] = level_width - wall_thickness

	def get_walls(self):
		wall_list = pygame.sprite.Group()

		#Left Side wall
		wall = Wall.Wall(0, 0, self.wall_thickness, 600)
		wall_list.add(wall)

		#Top wall
		wall = Wall.Wall(10, 0, 790, self.wall_thickness)
		wall_list.add(wall)

		#Small ledge
		wall = Wall.Wall(10, 200, 100, self.wall_thickness)
		wall_list.add(wall)

		#Right Side Wall
		wall = Wall.Wall(self.right_wall_x_pos, 0, self.wall_thickness, 600)
		wall_list.add(wall)

		wall = Wall.Wall(0, 590, 800, self.wall_thickness)
		wall_list.add(wall)

		return wall_list