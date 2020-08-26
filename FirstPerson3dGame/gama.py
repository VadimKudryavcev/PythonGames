import pygame
import math
from settings import *
from player import *
from map import *
from raycasting import *

sc = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()
player = Player()
pygame.font.init()

runGame = True
while runGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runGame = False
			break
	#background
	sc.fill(BLACK)
	pygame.draw.rect(sc, FLOOR, (0, HALF_HEIGHT, WIDHT, HALF_HEIGHT))
	pygame.draw.rect(sc, SKY, (0, 0, WIDHT, HALF_HEIGHT))
	
	#raycasting
	rayCasting(sc, player.pos, player.angle)

	#minimap
	pygame.draw.rect(sc, BLACK, (0, int(HEIGHT - HEIGHT * MAP_SCALE), int(WIDHT * MAP_SCALE), int(HEIGHT * MAP_SCALE)))
	for x,y in world_map:
		mx = x
		my = y
		pygame.draw.rect(sc, RED, (int(mx * MAP_SCALE), int(HEIGHT - HEIGHT * MAP_SCALE + my * MAP_SCALE), int(TILE * MAP_SCALE), int(TILE * MAP_SCALE)), 1)
	pygame.draw.circle(sc, RED, (int(player.x * MAP_SCALE), int(HEIGHT - HEIGHT * MAP_SCALE + player.y * MAP_SCALE)), int(player_radius * 2 * MAP_SCALE))
	pygame.draw.line(sc, WHITE, (int(player.x * MAP_SCALE), 
		                         int(HEIGHT - HEIGHT * MAP_SCALE + player.y * MAP_SCALE)), 
		                        (int((player.x + 30 * math.cos(player.angle)) * MAP_SCALE), 
		                         int(HEIGHT - HEIGHT * MAP_SCALE + (player.y + 30 * math.sin(player.angle)) * MAP_SCALE))
		              )

	#fps_counter
	fps_data = str(int(clock.get_fps()))
	f1 = pygame.font.SysFont('System', 36)
	fps_text = f1.render(fps_data, 0, WHITE)
	sc.blit(fps_text, (WIDHT - 35, 5))

	#player
	player.movement()

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()

	