import sys

#Initialize our drawing engine which will draw our images on the screen:
import pygame
from pygame.locals import *
from globals import *

pygame.init()

#Import our other game files:
from world import World
from assets import sprites

world = World(background=sprites["grass"])
player = world.load_level("levels/lvl1.txt")
world.setup()

resolution = ((world.size[1]+1)*SPRITE_SIZE, (world.size[0]+1)*SPRITE_SIZE)
screen = pygame.display.set_mode(resolution)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move('l')
            elif event.key == K_RIGHT:
                player.move('r')
            elif event.key == K_UP:
                player.move('u')
            elif event.key == K_DOWN:
                player.move('d')

    world.update()

    #Draw background
    for i in range(world.size[0]+1):
        for j in range(world.size[1]+1):
            screen.blit(world.background, (j*SPRITE_SIZE,i*SPRITE_SIZE))
    #Draw objects
    for obj in world.objects:
        i,j = obj.coords
        screen.blit(obj.sprite, (j*SPRITE_SIZE,i*SPRITE_SIZE))
    pygame.display.update()

