""" Manages the levels """
import pygame
from modules.sprites import Wall

class WallManager:
	wall_properties = None

	def __init__(self):
		properties = dict(line.strip().split('=') for line in open('settings.ini'))

		self.wall_properties = {'wall_thickness': int(properties['WALL_THICKNESS']), 'level_width': int(properties['LEVEL_WIDTH']), 'level_height': int(properties['LEVEL_HEIGHT'])}	
		self.wall_properties['right_wall_x_pos'] = self.wall_properties['level_width'] - self.wall_properties['wall_thickness']
		self.wall_properties['top_wall_width'] = self.wall_properties['level_width'] - self.wall_properties['wall_thickness']
		self.wall_properties['bottom_wall_y_pos'] = self.wall_properties['level_height'] - self.wall_properties['wall_thickness']

	def get_walls(self):
		wall_list = pygame.sprite.Group()

		wall_file = open("resources/walls.txt", "r")

		for line in wall_file.read().splitlines():
			if not line or line.startswith("#"):
				continue

			line = line % self.wall_properties
			line_params = line.split(",")

			wall = Wall.Wall(line_params[0], line_params[1], line_params[2], line_params[3])

			wall_list.add(wall)

		wall_file.close()

		return wall_list