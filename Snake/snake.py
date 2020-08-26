import pygame
import random
pygame.init()
pygame.mixer.init()

def saveScore(s):
	f = open('score.txt', 'w')
	f.write(str(s))
	f.close()

def openScore():
	f = open('score.txt', 'r')
	f.seek(0)
	return f.read()
	f.close()

#main
D_WIDHT = 600
D_HEIGHT = 600
TILE = (D_WIDHT) // 20
SNAKE_SIZE = TILE - 2

#player
player_default_speed = TILE
recstr = openScore()
record = int(recstr)

#color
LGREEN = (100, 220, 100)
CHARCH = (30, 30, 30)

#fonts
pygame.font.init()
font1 = pygame.font.SysFont('Consolas', int(36 * TILE / 25))
font2 = pygame.font.SysFont('Consolas', int(18 * TILE / 25))

#music
pygame.mixer.music.load('snake.wav')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)

#sound
apple_sound = pygame.mixer.Sound('apple.wav')
new_record_sound = pygame.mixer.Sound('newrecord.wav')

sc = pygame.display.set_mode((D_WIDHT, D_HEIGHT))
clock = pygame.time.Clock()
startGame = True

while startGame:
	sc.fill(LGREEN)

	pygame.mixer.music.set_volume(1)

	runGame = True
	x, y = random.randint(100, D_WIDHT-100), random.randint(100, D_HEIGHT-100)
	apple_x, apple_y = random.randint(0, D_WIDHT), random.randint(0, D_HEIGHT)
	speed_y = 0
	speed_x = 0
	snake_list = []
	length_of_snake = 1
	FPS = 2
	sound_wasnt_played = True

	while runGame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runGame = False
				break

		sc.fill(LGREEN)

		#game speed
		K_FPS = int(FPS)

		#player
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] and (not speed_y > 0):
			speed_y = -player_default_speed
			speed_x = 0
		if keys[pygame.K_s] and (not speed_y < 0):
			speed_y = player_default_speed
			speed_x = 0
		if keys[pygame.K_a] and (not speed_x > 0):
			speed_y = 0
			speed_x = - player_default_speed
		if keys[pygame.K_d] and (not speed_x < 0):
			speed_y = 0
			speed_x = player_default_speed
		if keys[pygame.K_SPACE]:
			K_FPS *= 2
		if keys[pygame.K_q]:
			startGame = False
			runGame = False

		#change position of head
		y += speed_y
		x += speed_x

		#tails list
		snake_head = []
		snake_head.append(x)
		snake_head.append(y)
		snake_list.append(snake_head)
		if len(snake_list) > length_of_snake:
			del snake_list[0]

		#collision with tail
		for dot in snake_list[:-1]:
				if dot == snake_head:
					runGame = False
					record = length_of_snake - 1
					saveScore(str(record))

		#collision with wall
		if (x < 0) or (x > D_WIDHT) or (y < 0) or (y > D_HEIGHT):
			runGame = False
			record = length_of_snake - 1
			saveScore(str(record))

		#draw apple
		pygame.draw.rect(sc, CHARCH, ((apple_x // TILE * TILE + 5) , (apple_y // TILE * TILE  + 5), SNAKE_SIZE - 9, SNAKE_SIZE - 9), 2)

		#draw snake
		for dot in snake_list:
			pygame.draw.rect(sc, CHARCH, ((dot[0] // TILE * TILE + 1) , (dot[1] // TILE * TILE  + 1), SNAKE_SIZE, SNAKE_SIZE))
		
		#apple eating
		if ((x // TILE * TILE == apple_x // TILE * TILE) and (y // TILE * TILE == apple_y // TILE * TILE)):
			length_of_snake += 1
			apple_x, apple_y = random.randint(0, D_WIDHT), random.randint(0, D_HEIGHT)
			FPS += 0.2
			apple_sound.play()

		#score text
		score_text = font2.render(str(length_of_snake - 1), 0, CHARCH)
		if not (speed_x == speed_y):
			sc.blit(score_text, (D_WIDHT - 40, 6))

		#start text
		if (speed_x == speed_y):
			sc.fill(LGREEN)
			start_text = font1.render('PRESS WASD TO START', 0, CHARCH)
			sc.blit(start_text, (20, D_HEIGHT // 2 -15))
			record_text = font1.render('MAX SCORE IS ' + str(record), 0, CHARCH)
			sc.blit(record_text, (20, D_HEIGHT // 2 + 15))
			info_text = font2.render('Press SPACE to speed up. Press Q to QUIT.', 0, CHARCH)
			sc.blit(info_text, (20, D_HEIGHT - 20))

		#sound		
		if (speed_x == speed_y):
			pygame.mixer.music.set_volume(1)
		else:
			pygame.mixer.music.set_volume(0)

		if (length_of_snake - 1 > record) and sound_wasnt_played:
			new_record_sound.play()
			sound_wasnt_played = False

		pygame.display.update()
		clock.tick(K_FPS)
	pygame.display.update()
pygame.quit()
