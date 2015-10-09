imagecloud="cloud.png"
imagebckgrd="background.png"
imagestones="stone.png"

import pygame,sys
from pygame.locals import *

pygame.init()
Screen=pygame.display.set_mode((840,640),0,32)
background=pygame.image.load(imagebckgrd).convert()
cloud=pygame.image.load(imagecloud).convert_alpha()
stone=pygame.image.load(imagestones).convert_alpha()
x=0
y=0
z=0
pygame.display.update()
clock=pygame.time.Clock()
speed=250

while True :

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()


    Screen.blit(background,(0,0))
    #Screen.blit(stone,(220,220))
    Screen.blit(stone,(420,320))
    
    Screen.blit(stone,(z,120))
    
    Screen.blit(stone,(y,220))
    
    #Screen.blit(cloud,(x,10))
    x=x+1
    y=y+ 0.4
    z=z+0.8

    if x>840 :
        x=0

    if y>840:
        y=0

    if z>840:
        z=0

    

    pygame.display.update()


