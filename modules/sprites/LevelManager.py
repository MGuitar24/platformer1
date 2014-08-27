""" Loads levels """

from modules.sprites import EntityManager

class LevelManager:
	base_filepath = "resources/levels/level"
	extension = ".txt"

	all_sprite_group = None
	current_level_walls = None
	current_level_entities = None

	def __init__(self, all_sprite_group, wall_group, proximity_sprite_list):
		self.all_sprite_group = all_sprite_group
		self.wall_group = wall_group
		self.proximity_sprite_list = proximity_sprite_list

	def load_level(self, level_number):
		level_number = str(level_number)

		self.__remove_old_sprites()

		wall_filepath = self.base_filepath + level_number + "_walls"+ self.extension
		entity_filepath = self.base_filepath + level_number + "_entities"+ self.extension

		entity_manager = EntityManager.EntityManager(wall_filepath, entity_filepath)

		self.current_level_walls = entity_manager.get_walls()
		self.current_level_entities = entity_manager.get_entities()

		self.all_sprite_group.add(self.current_level_walls)
		self.all_sprite_group.add(self.current_level_entities)

		self.wall_group.add(self.current_level_walls)
		self.proximity_sprite_list.extend(self.current_level_entities)

	def __remove_old_sprites(self):
		if self.current_level_walls and self.current_level_walls and self.all_sprite_group:
			self.all_sprite_group.remove(self.current_level_walls)
			self.all_sprite_group.remove(self.current_level_entities)
			
			self.wall_group.remove(self.current_level_walls)
			self.proximity_sprite_list = [x for x in self.proximity_sprite_list if x not in self.current_level_entities]