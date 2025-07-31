from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()       # initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set up screen object as a display
    clock = pygame.time.Clock() # set up clock object

    updatable = pygame.sprite.Group() #creates updatable group
    drawable = pygame.sprite.Group()    # creates drawable group
    asteroid = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroid ,updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable ) # put both groups into the Player container
    Shot.containers = (shots, updatable, drawable)


    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # creates a Player object called player, because it is made after containers were declared it is added to the groups.
    dt = 0      # delta time
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:                               # Game Loop
        for event in pygame.event.get():      # quit sequence   
            if event.type == pygame.QUIT:
                return

        
        updatable.update(dt)        # calls update on all objects in updatable group

        for object in asteroid:       # collision distruction
            if object.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:      # shot distroying asteroid
                if shot.collision(object):
                    object.split(object)
                    shot.kill()

        

        screen.fill("black", rect=None, special_flags=0)    # pygame method that colors the screen

        for object in drawable:   # Iterates and draws each object in drawable group
            object.draw(screen)
        
        pygame.display.flip()
       
        dt = clock.tick(60) / 1000  #sets delta time

if __name__ == "__main__":      # This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module. 
    main()
