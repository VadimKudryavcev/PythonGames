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
pygame.mixer.init()

kick_sound = pygame.mixer.Sound('kick.wav')
kick2_sound = pygame.mixer.Sound('kick2.wav')

pygame.mixer.music.load('pythonosutest.mp3')
pygame.mixer.music.set_volume(1)

startGame = True
score = 0
combo_num = 0
time0 = time.time() * 10
cur_circle_num = 0
music_playing = False
j = 0
tt = 8
point_for_drawing = ''
pos_for_point = (0, 0)
number = 0

circle_num = 102
circle_awake_time = 30
music_start_time = circle_awake_time - 3

#map
f = open('tempmap.txt', 'r')
temp_map = f.readlines()
circles = []
for i in range(0, circle_num):
	x = random.randint(CIRCLE_RADIUS, D_WIDHT - CIRCLE_RADIUS)
	y = random.randint(CIRCLE_RADIUS, D_HEIGHT - CIRCLE_RADIUS)
	if (i >= 42 and i <= 49) or (i >= 91 and i <= 100):
		x = int(500 + 150 * math.cos(i/2))
		y = int(250 + 150 * math.sin(i/2))
	number += 1
	if number == 6:
		number = 1
	circle = Circle(x, y, circle_awake_time, True, str(number))
	circle_awake_time += int(temp_map[i])
	circles.append(circle)

while startGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			startGame = False
			break

	if (time.time() * 10 - time0 >=  music_start_time) and not music_playing:
		pygame.mixer.music.play(loops=-1)
		music_playing = True

	#drawing
	drawingBackground(sc)
	drawingText(sc, font1, score, combo_num)
	for i in range(0, circle_num):
		current_circle = circles[i]

		drawingCircle(sc, current_circle.pos, current_circle.awake_time, time.time() * 10 - time0, current_circle.state, font1, current_circle.num)
		drawingPoint(sc, pos_for_point, point_for_drawing, font1)

	#mouse position
	pos = pygame.mouse.get_pos()
	mouse_x = pos[0]
	mouse_y = pos[1]

	if cur_circle_num > circle_num - 1:
		break
	cur_circle = circles[cur_circle_num]
	x = cur_circle.x
	y = cur_circle.y
	time1 = time.time() * 10 - time0 #current time
	dtime = cur_circle.awake_time - time1
	circleAlive = True

	keys = pygame.key.get_pressed()
	if (keys[pygame.K_z] or keys[pygame.K_x]) and key_not_pressed:
		if (dtime >= 0) and (dtime <= CIRCLE_LIVE):
			if (mouse_y < y + CIRCLE_RADIUS) and (mouse_y > y - CIRCLE_RADIUS) and (mouse_x < x + CIRCLE_RADIUS) and (mouse_x > x - CIRCLE_RADIUS):
				cur_circle.state = False
				combo_num += 1
				coef = 3 * dtime / CIRCLE_LIVE
				point = 100 * (3 - int(coef))
				point_mult = point * combo_num
				score += point_mult
				cur_circle_num += 1
				if dtime < CIRCLE_LIVE / 3:
					kick_sound.play()
				else:
					kick2_sound.play()
				point_for_drawing = str(point)
				pos_for_point = (x, y)
		key_not_pressed = False

	if not (keys[pygame.K_z] or keys[pygame.K_x]):
		key_not_pressed = True

	if dtime < 0:
		cur_circle_num += 1
		combo_num = 0
		point_for_drawing = 'X'
		pos_for_point = (x, y)

	pygame.display.update()