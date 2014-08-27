""" Loads levels """

from modules.sprites import EntityManager
from modules.sprites import Background

class LevelManager:
	level_base_filepath = "resources/levels/level"
	level_extension = ".txt"

	background_base_filepath = "resources/spritemaps/BACKGROUND_level_"
	background_extension = ".png"

	all_sprite_group = None
	current_level_walls = None
	current_level_entities = None

	def __init__(self, all_sprite_group, wall_group, proximity_sprite_list, background, player):
		self.all_sprite_group = all_sprite_group
		self.wall_group = wall_group
		self.proximity_sprite_list = proximity_sprite_list
		self.background = background
		self.player = player

		self.all_sprite_group.add(self.player)

	def load_level(self, level_number):
		level_number = str(level_number)

		wall_filepath = self.level_base_filepath + level_number + "_walls"+ self.level_extension
		entity_filepath = self.level_base_filepath + level_number + "_entities"+ self.level_extension

		entity_manager = EntityManager.EntityManager(wall_filepath, entity_filepath)

		self.current_level_walls = entity_manager.get_walls()
		self.current_level_entities = entity_manager.get_entities()

		self.__reload_sprites()
		self.__update_background(level_number)
		self.__move_player(level_number)

	def __update_background(self, level_number):
		self.background.change_background(self.background_base_filepath + level_number + self.background_extension)

	def __move_player(self, level_number):
		properties_file = open(self.level_base_filepath + level_number + "_properties" + self.level_extension, "r")

		for line in properties_file.read().splitlines():
			if not line or line.startswith("#"):
				continue

		line_params = line.split(",")

		if "player" == line_params[0]:
			self.player.change_location(int(line_params[1]), int(line_params[2]))
			self.player.walls = self.wall_group

		properties_file.close()

	def __reload_sprites(self):
		if self.current_level_walls and self.current_level_walls and self.all_sprite_group:
			self.all_sprite_group.remove(self.current_level_walls)
			self.all_sprite_group.remove(self.current_level_entities)

			self.wall_group.remove(self.current_level_walls)
			self.proximity_sprite_list = [x for x in self.proximity_sprite_list if x not in self.current_level_entities]

		self.all_sprite_group.add(self.current_level_walls)
		self.all_sprite_group.add(self.current_level_entities)

		self.wall_group.add(self.current_level_walls)
		self.proximity_sprite_list.extend(self.current_level_entities)