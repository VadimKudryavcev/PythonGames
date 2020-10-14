import pygame
from settings import *

pygame.font.init()
pygame.init()

def drawingBackground(sc):
	sc.fill((0, 0, 0))

def drawingText(sc, font, score, combo_num):
	score_text = font.render(str(score), 0, (250, 250, 250))
	sc.blit(score_text, (20, D_HEIGHT - 30))
	combo_text = font.render('x'+str(combo_num), 0, (250, 250, 250))
	sc.blit(combo_text, (20, D_HEIGHT - 60))

def drawingCircle(sc, pos, awake_time, timer, state, font, num):
	x, y = pos
	if (timer >= awake_time - CIRCLE_LIVE) and (timer <= awake_time) and state:
		c1 = 10 * (timer - awake_time)
		pygame.draw.circle(sc, (200, 200, 50), (x, y), CIRCLE_RADIUS)
		rad = CIRCLE_RADIUS - int(c1) - 25
		if rad > CIRCLE_RADIUS + 2:
			CONTOUR_CIRCLE_RADIUS = rad
		else:
			CONTOUR_CIRCLE_RADIUS = CIRCLE_RADIUS + 2
		pygame.draw.circle(sc, (200, 200, 100 + 20), (x, y), CONTOUR_CIRCLE_RADIUS, 2) 
		text = font.render(num, 0, (0, 0, 0))
		sc.blit(text, (x - 5, y - 10))

def drawingPoint(sc, pos, point, font):
	x, y = pos
	if point == '300':
		color = (50, 150, 250)
	elif point == '200':
		color = (50, 250, 100)
	elif point == '100':
		color = (100, 250, 50)
	else:
		color = (250, 0, 0)
	text = font.render(point, 0, color)
	sc.blit(text, (x - 30, y - 5))


