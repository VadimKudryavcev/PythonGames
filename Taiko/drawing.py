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

def drawingCircle(sc, pos, awake_time, timer, state, font):
	x, y = pos
	if (timer >= awake_time - CIRCLE_LIVE) and (timer <= awake_time) and state:
		c1 = 10 * (CIRCLE_LIVE + timer - awake_time) // 20 * 20
		pygame.draw.circle(sc, (150 + c1, c1, 0), (x, y), CIRCLE_RADIUS) 
		if awake_time - timer < 5:
			text = font.render('CLICK', 0, (0, 0, 0))
			sc.blit(text, (x - 30, y - 5))

def drawingPoint(sc, pos, point, font):
	x, y = pos
	text = font.render(str(point), 0, (0, 100, 100))
	sc.blit(text, (x - 30, y - 5))


