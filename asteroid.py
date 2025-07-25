from circleshape import CircleShape
import pygame
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
       

    def draw(self, screen):  # learned not to pass too much into the method. 
        pygame.draw.circle(screen, "white",self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt