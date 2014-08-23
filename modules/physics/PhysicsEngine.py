class PhysicsEngine:
	def __init__(self):
		self.gravity = 1
	def applyGravity(self, gravitable):
		#for gravitable in gravityObjects:
		gravitable.applyGravity()