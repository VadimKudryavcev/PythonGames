import pygame
import math
from settings import *
from player import *
from map import *
from raycasting import *

sc = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()
player = Player()

runGame = True
while runGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runGame = False
	#background
	sc.fill(BLACK)
	pygame.draw.rect(sc, FLOOR, (0, HALF_HEIGHT, WIDHT, HALF_HEIGHT))
	pygame.draw.rect(sc, SKY, (0, 0, WIDHT, HALF_HEIGHT))
	#for x,y in world_map:
	#	pygame.draw.rect(sc, WHITE, (x, y, TILE, TILE))

	#raycasting
	rayCasting(sc, player.pos, player.angle)

	#player
	player.movement()
	#pygame.draw.circle(sc, RED, (int(player.x), int(player.y)), player_radius)
	#pygame.draw.line(sc, RED, (int(player.x), int(player.y)), (player.x + WIDHT * math.cos(player.angle),
	#	                                      				   player.y + WIDHT * math.sin(player.angle)))
	
	

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()

	