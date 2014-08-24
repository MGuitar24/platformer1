BLACK = (0, 0, 0)
class SpritesheetUtility:
	def animationFramesLoader(self, startX, imageY, width, height, magicNumber, spriteMap):
		animationFrames = []
		for i in range(9):
			animationFrames.append(spriteMap.image_at((startX + i * magicNumber, imageY, width, height), colorkey=BLACK))
		return animationFrames