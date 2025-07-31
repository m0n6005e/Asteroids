from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
       

    def draw(self, screen):  # learned not to pass too much into the method. 
        pygame.draw.circle(screen, "white",self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, object):
        object.kill()
        if object.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            asteroid_1_velocity = pygame.math.Vector2.rotate(object.velocity, - random_angle) 
            asteroid_2_velocity = pygame.math.Vector2.rotate(object.velocity, + random_angle)
            new_asteroid_radius = object.radius - ASTEROID_MIN_RADIUS
            
            asteroid_1 = Asteroid(object.position.x, object.position.y, new_asteroid_radius)
            asteroid_1.velocity = asteroid_1_velocity * 1.2

            asteroid_2 = Asteroid(object.position.x, object.position.y, new_asteroid_radius)
            asteroid_2.velocity = asteroid_2_velocity * 1.2
            