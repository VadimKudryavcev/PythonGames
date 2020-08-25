import pygame
import math
from settings import *
from player import *
from map import *

def rayCasting(sc, player_pos, player_angle):
	current_angle = player_angle - HALF_FOV
	current_x, current_y = player_pos
	for i in range(NUM_RAYS):
		sin_a = math.sin(current_angle)
		cos_a = math.cos(current_angle)
		for j in range(SEE_DEPTH):
			x = current_x + j * cos_a
			y = current_y + j * sin_a
			#pygame.draw.line(sc, GREEN, player_pos, (x, y))
			if (x // TILE * TILE, y // TILE * TILE) in world_map:
				j *= math.cos(player_angle - current_angle)
				wall_height = COEF / j
				c = 255 / (1 + j * 0.01)
				color = (c, c // 3, c // 2)
				pygame.draw.rect(sc, color, (i * WIDHT_SCALE, HALF_HEIGHT - wall_height // 2, WIDHT_SCALE, wall_height))
				break
		current_angle += RAY_ANGLE
		