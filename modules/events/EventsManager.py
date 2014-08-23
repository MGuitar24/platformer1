import pygame

class EventsManager:
	def __init__(self, playableCharacter):
		self.playableCharacter = playableCharacter

	def determineEvent(self, event):
		done = False
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
			if event.key == pygame.K_LEFT:
				self.playableCharacter.changespeed(-1, 0)
			elif event.key == pygame.K_RIGHT:
				self.playableCharacter.changespeed(1, 0)
			elif event.key == pygame.K_UP:
				self.playableCharacter.changespeed(0, -1)
			elif event.key == pygame.K_DOWN:
				self.playableCharacter.changespeed(0, 1)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.playableCharacter.changespeed(1, 0)
			elif event.key == pygame.K_RIGHT:
				self.playableCharacter.changespeed(-1, 0)
			elif event.key == pygame.K_UP:
				self.playableCharacter.changespeed(0, 1)
			elif event.key == pygame.K_DOWN:
				self.playableCharacter.changespeed(0, -1)
		return done