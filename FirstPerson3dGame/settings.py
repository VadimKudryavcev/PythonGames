import math

#settings
WIDHT = 500
HEIGHT = 500
HALF_WIDHT = WIDHT // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 50
MAP_SCALE = 0.2

#ray_casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 250
SEE_DEPTH = 500
RAY_ANGLE = FOV / NUM_RAYS
SCREEN_DIST = 2 / math.tan(HALF_FOV)
COEF = 3500 * SCREEN_DIST
WIDHT_SCALE = WIDHT // NUM_RAYS

#player
player_pos = (HALF_WIDHT, HALF_HEIGHT)
player_vel = 1
player_angle = 0
player_radius = 10
player_turnSpeed = 0.05

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (220, 0, 0)
GREEN = (0, 220, 0)

SKY = (200, 70, 30)
FLOOR = (50, 50, 50)