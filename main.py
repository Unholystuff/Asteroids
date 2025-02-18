import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    ##Player setup
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/ 2) 
    dt = 0

    ##Asteroid setup
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    ##AsteroidField setup
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    ##Shots setup 
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/ 1000
        updatable.update(dt)
        for asteroid in asteroids:
             if asteroid.collision(player):
                  print("Game over!")
                  sys.exit()
        for asteroid in asteroids:
             for shot in shots:
                  if asteroid.collision(shot):
                    shot.kill()
                    asteroid.kill()

if __name__ == "__main__":
    main()