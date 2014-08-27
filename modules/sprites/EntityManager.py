""" Manages the levels """
import pygame
from modules.sprites import Wall
from modules.sprites import Chest

class EntityManager:
	def __init__(self, wall_filename, entity_filename):
		self.wall_filename = wall_filename
		self.entity_filename = entity_filename

		properties = dict(line.strip().split('=') for line in open('settings.ini'))

		self.__initialize_wall_properties(properties)
		self.__initialize_entity_properties(properties)

	def __initialize_wall_properties(self, properties):
		self.wall_properties = {'wall_thickness': int(properties['WALL_THICKNESS']), 'level_width': int(properties['LEVEL_WIDTH']), 'level_height': int(properties['LEVEL_HEIGHT'])}	
		self.wall_properties['right_wall_x_pos'] = self.wall_properties['level_width'] - self.wall_properties['wall_thickness']
		self.wall_properties['top_wall_width'] = self.wall_properties['level_width'] - self.wall_properties['wall_thickness']
		self.wall_properties['bottom_wall_y_pos'] = self.wall_properties['level_height'] - self.wall_properties['wall_thickness']

	def __initialize_entity_properties(self, properties):
		self.entity_properties = {'chest_filename': properties['CHEST_FILENAME']}

	def get_walls(self):
		wall_list = pygame.sprite.Group()

		wall_file = open(self.wall_filename, "r")

		for line in wall_file.read().splitlines():
			if not line or line.startswith("#"):
				continue

			line = line % self.wall_properties
			line_params = line.split(",")

			wall = Wall.Wall(line_params[0], line_params[1], line_params[2], line_params[3])

			wall_list.add(wall)

		wall_file.close()

		return wall_list

	def get_entities(self):
		entity_list = pygame.sprite.Group()

		entity_file = open(self.entity_filename, "r")

		for line in entity_file.read().splitlines():
			if not line or line.startswith("#"):
				continue

			line = line % self.entity_properties
			line_params = line.split(",")

			if "chest" == line_params[0]:
				entity = Chest.Chest(int(line_params[1]), int(line_params[2]), line_params[3])
				entity_list.add(entity)

		return entity_list