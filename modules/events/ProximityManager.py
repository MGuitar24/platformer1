class ProximityManager:
	def __init__(self, players):
		self.players = players

	def checkProximityToPlayers(self, entities):
		# TODO: Make sure to add threshold to the objects.
		for player in players:
			(radius, x, y) = self.calculateObjectRadiusAndCenterpoint();

	def calculateObjectRadiusAndCenterpoint(self, entity):
		width = entity.iWidth
		height = entity.iHeight

