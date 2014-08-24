""" Loads levels """

class LevelManager:
	def load_level(self, level_number):
		level = open("resources/level/level"+ level_number +".txt", "r")

		level.close()