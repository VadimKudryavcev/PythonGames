import pygame
import random
import math

#Set
NUM_PARTICLES = 500
NUM_ORIGIN = 20
WIDHT = 1000
HEIGHT = 500
FPS = 10
gravity = 2
size_change = 0.8
SIZE_1 = 20
SIZE_2 = 2
SPEED_1 = 0
SPEED_2 = 30

#color
BLACK = (0, 0, 0)

particles = []

sc = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			break

	particles.clear()
	lenght_of_list = 0	
	COUNT = 0
	firstInit = True

	while True:
		sc.fill(BLACK)
		x0 = random.randint(20, WIDHT - 20)
		y0 = random.randint(20, HEIGHT - 20)
		print(str(lenght_of_list))

		color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
		for i in range(NUM_PARTICLES * (COUNT - 1), NUM_PARTICLES * COUNT, 1):
			size_part = SIZE_1 + SIZE_2 * random.random()
			speed_part = SPEED_1 + SPEED_2 * random.random()
			angle_part = 2 * math.pi * random.random()
			x = x0
			y = y0
			pack = [x, y, size_part, speed_part, angle_part, color]
			if firstInit:
				particles.insert(i, pack)
				lenght_of_list += 1
			else: 
				particles[i] = pack

		for i in range(lenght_of_list):
			part = particles[i]
			if (part[2] > 1) or (part[0] > WIDHT) or (part[0] < 0) or (part[1] > HEIGHT):
				pygame.draw.circle(sc, part[5], (int(part[0]), int(part[1])), int(part[2]))
				cos_a = math.cos(part[4])
				dx = part[3] * cos_a

				sin_a = math.sin(part[4])
				dy = part[3] * sin_a

				dy += gravity

				part[0] += dx
				part[1] += dy

				part[3] = (dx ** 2 + dy ** 2) ** (1 / 2)
				if (dx > 0):
					part[4] = math.atan(dy / (dx + 0.0001))
				else:
					part[4] = math.pi + math.atan(dy / (dx + 0.0001))

				if part[2] > 1:
			   		part[2] *= size_change

		COUNT += 1
		if (COUNT > NUM_ORIGIN):
			COUNT = 0
			firstInit = False

		pygame.display.update()
		clock.tick(FPS)
pygame.quit()	