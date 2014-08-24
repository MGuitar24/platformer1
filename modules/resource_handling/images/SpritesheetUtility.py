class SpritesheetUtility:
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	def animationFramesLoader(self, startX, imageY, width, height, magicNumber, spriteMap):
		animationFrames = []
		for i in range(9):
			animationFrames.append(spriteMap.image_at((startX + i * magicNumber, imageY, width, height), colorkey=self.BLACK))
		return animationFrames