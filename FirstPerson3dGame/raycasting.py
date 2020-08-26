import pygame
import math
from settings import *
from player import *
from map import *

def getMapCoord(x, y):
	return (x // TILE * TILE, y // TILE * TILE)

def rayCasting(sc, player_pos, player_angle):
	current_x, current_y = player_pos
	current_rect_x, current_rect_y = getMapCoord(current_x, current_y)
	current_angle = player_angle - HALF_FOV
	for i in range(NUM_RAYS):
		sin_a = math.sin(current_angle)
		cos_a = math.cos(current_angle)
		
		#coord of verticals
		if cos_a >= 0:
			x = current_rect_x + TILE
			dx = 1
		else:
			x = current_rect_x
			dx = -1
		for j in range(0, WIDHT, TILE):
			depth_vert = (x - current_x) / cos_a
			y = current_y + depth_vert * sin_a
			if getMapCoord(x + dx, y) in world_map:
				#pygame.draw.line(sc, GREEN, player_pos, (x, y), 2)
				break
			x += dx * TILE 

		#coord of horizontal
		if sin_a >= 0:
			y = current_rect_y + TILE
			dy = 1
		else:
			y = current_rect_y
			dy = -1
		for j in range(0, HEIGHT, TILE):
			depth_hori = (y - current_y) / sin_a
			x = current_x + depth_hori * cos_a
			if getMapCoord(x, y + dy) in world_map:
				#pygame.draw.line(sc, RED, player_pos, (x, y), 2)
				break
			y += dy * TILE 

		#drawing
		if depth_vert < depth_hori:
			depth = depth_vert
		else:
			depth = depth_hori
		depth *= math.cos(player_angle - current_angle)
		wall_height = COEF / depth
		c = 255 / (1 + depth * 0.01)
		color = (c, c // 3, c // 2)
		pygame.draw.rect(sc, color, (i * WIDHT_SCALE, HALF_HEIGHT - wall_height // 2, WIDHT_SCALE, wall_height))
		current_angle += RAY_ANGLE


		