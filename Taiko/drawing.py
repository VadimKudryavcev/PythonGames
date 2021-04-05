import pygame 
from settings import *

pygame.font.init()
pygame.init()

class Drawing:
	def __init__(self, sc):
		self.sc = sc
		self.BG = pygame.image.load(BG_ROOT).convert()

	def drawingBackground(self):
		self.sc.blit(self.BG, (0, 0))

	def drawingText(self, font, score, combo_num):
		score_text = font.render(str(score), 0, WHITE)
		self.sc.blit(score_text, (20, D_HEIGHT - 30))
		combo_text = font.render('x'+str(combo_num), 0, WHITE)
		self.sc.blit(combo_text, (20, D_HEIGHT - 60))

	def drawingCircle(self, pos, awake_time, timer, state, font, num):
		x, y = pos
		if (timer >= awake_time - CIRCLE_LIVE) and (timer <= awake_time) and state:
			c1 = 10 * (timer - awake_time)
			pygame.draw.circle(self.sc, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)
			rad = CIRCLE_RADIUS - int(c1) - 25
			if rad > CIRCLE_RADIUS + 2:
				CIRCLE_CONTOUR_RADIUS = rad
			else:
				CIRCLE_CONTOUR_RADIUS = CIRCLE_RADIUS + 2
			pygame.draw.circle(self.sc, CIRCLE_CONTOUR_COLOR, (x, y), CIRCLE_CONTOUR_RADIUS, 2) 
			text = font.render(num, 0, BLACK)
			self.sc.blit(text, (x - 5, y - 10))

	def drawingPoint(self, pos, point, font):
		x, y = pos
		text = font.render(point, 0, SCORE_COLOR_DICT.get(point))
		self.sc.blit(text, (x - 30, y - 5))


