from settings import *

class Circle:
	def __init__(self, x, y, circle_awake_time, state):
		self.x = x
		self.y = y
		self.awake_time = circle_awake_time
		self.state = state

	@property
	def pos(self):
		return (self.x, self.y)

	