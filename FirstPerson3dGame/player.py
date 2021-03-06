import pygame
import math
from settings import *

class Player:
	def __init__(self):
		self.x, self.y = player_pos
		self.angle = player_angle

	@property
	def pos(self):
		return (self.x, self.y)

	def movement(self):
		sin_angle = math.sin(self.angle)
		cos_angle = math.cos(self.angle)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LSHIFT]:
			shift = 2
		else:
			shift = 1
		if keys[pygame.K_w]:
			self.y += shift * player_vel * sin_angle
			self.x += shift * player_vel * cos_angle
		if keys[pygame.K_s]:
			self.y -= shift * player_vel * sin_angle
			self.x -= shift * player_vel * cos_angle
		if keys[pygame.K_a]:
			self.y -= shift * player_vel * cos_angle
			self.x += shift * player_vel * sin_angle
		if keys[pygame.K_d]:
			self.y += shift * player_vel * cos_angle
			self.x -= shift * player_vel * sin_angle
		if keys[pygame.K_LEFT]:
			self.angle -= player_turnSpeed
		if keys[pygame.K_RIGHT]:
			self.angle += player_turnSpeed