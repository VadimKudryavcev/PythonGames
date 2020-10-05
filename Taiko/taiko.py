import pygame
import random
import time
import math
from settings import *
from drawing import *
from circle import *

sc = pygame.display.set_mode((D_WIDHT, D_HEIGHT))
clock = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.SysFont('Consolas', int(24))

#временно тут
pygame.mixer.init()
kick_sound = pygame.mixer.Sound('kick.wav')
kick2_sound = pygame.mixer.Sound('kick2.wav')

#pygame.mixer.music.load('test3.mp3')
#pygame.mixer.music.set_volume(1)
#потом

startGame = True
score = 0
combo_num = 0
time0 = time.time() * 10
cur_circle_num = 0
music_playing = False
j = 0
tt = 8

circle_num = 100
circle_awake_time = 10

circles = []
for i in range(0, circle_num):
	x = random.randint(CIRCLE_RADIUS, D_WIDHT - CIRCLE_RADIUS)
	y = random.randint(CIRCLE_RADIUS, D_HEIGHT - CIRCLE_RADIUS)
	#x = int(500 + 150 * math.cos(i/2))
	#y = int(250 + 150 * math.sin(i/2))
	circle = Circle(x, y, circle_awake_time, True)
	if j == 3:
		tt = 4
	elif j == 4:
		tt = 4
		j = 0
	else:
		tt = 8
	circle_awake_time += tt
	j += 1
	circles.append(circle)

while startGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			startGame = False
			break

	#if (time.time() * 10 - time0 >= 10 + CIRCLE_LIVE) and not music_playing:
	#	pygame.mixer.music.play(loops=-1)
	#	music_playing = True

	#drawing
	drawingBackground(sc)
	drawingText(sc, font1, score, combo_num)
	for i in range(0, circle_num):
		current_circle = circles[i]
		drawingCircle(sc, current_circle.pos, current_circle.awake_time, time.time() * 10 - time0, current_circle.state, font1)

	pos = pygame.mouse.get_pos()
	mouse_x = pos[0]
	mouse_y = pos[1]

	cur_circle = circles[cur_circle_num]
	x = cur_circle.x
	y = cur_circle.y
	time1 = time.time() * 10 - time0
	dtime = cur_circle.awake_time - time1
	circleAlive = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_z] or keys[pygame.K_x]:
		if (dtime >= 0) and (dtime <= CIRCLE_LIVE):
			if (mouse_y < y + CIRCLE_RADIUS) and (mouse_y > y - CIRCLE_RADIUS) and (mouse_x < x + CIRCLE_RADIUS) and (mouse_x > x - CIRCLE_RADIUS):
				cur_circle.state = False
				combo_num += 1
				coef = 3 * dtime / CIRCLE_LIVE
				point = 100 * (4 - int(coef))
				point_mult = point * combo_num
				score += point
				cur_circle_num += 1
				if dtime < 5:
					kick_sound.play()
				else:
					kick2_sound.play()

	if dtime < 0:
		cur_circle_num += 1
		combo_num = 0
	
	pygame.display.update()

"""
Улучшения:
Класс для круга с координатами, временем жизни, временем пробуждения, и состояние (alive or not)
"""