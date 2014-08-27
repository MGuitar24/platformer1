""" Manages the levels """
import pygame
from modules.sprites import Wall

class WallManager:
	def __init__(self, wall_filename):
		self.wall_filename = wall_filename

		properties = dict(line.strip().split('=') for line in open('settings.ini'))

		self.wall_properties = {'wall_thickness': int(properties['WALL_THICKNESS']), 'level_width': int(properties['LEVEL_WIDTH']), 'level_height': int(properties['LEVEL_HEIGHT'])}	
		self.wall_properties['right_wall_x_pos'] = self.wall_properties['level_width'] - self.wall_properties['wall_thickness']
		self.wall_properties['top_wall_width'] = self.wall_properties['level_width'] - self.wall_properties['wall_thickness']
		self.wall_properties['bottom_wall_y_pos'] = self.wall_properties['level_height'] - self.wall_properties['wall_thickness']

	def get_walls(self):
		wall_list = pygame.sprite.Group()

<<<<<<< HEAD
		wall_file = open(self.wall_filename, "r")
=======
		wall_file = open("resources/levels/walls.txt", "r")
>>>>>>> d0b30af29c3678010924b314f97d9d0a02ad7acd

		for line in wall_file.read().splitlines():
			if not line or line.startswith("#"):
				continue

			line = line % self.wall_properties
			line_params = line.split(",")

			wall = Wall.Wall(line_params[0], line_params[1], line_params[2], line_params[3])

			wall_list.add(wall)

		wall_file.close()

		return wall_list