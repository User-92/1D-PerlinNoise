import pygame,noise,random,os,sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Perlin Noise Testing")
screen = pygame.display.set_mode((500,500),0,32)

#change
#change2

def gen_noise_rect(x,y):
    height = noise.pnoise1(x * 0.1, repeat=999999999, base = 2, octaves=2) * 30
    return pygame.Rect(x,y-height,5,5)


def gen_noise():
    noises = []
    for y in range(1):
        y += 100
        for x in range(500):
            rect = gen_noise_rect(x, y)
            noises.append(rect)
    return noises

run_once = False
while True:
    screen.fill((0,0,0))

    if not run_once:
        noises = gen_noise()

    for rect in noises:
        pygame.draw.rect(screen, (255,255,255), rect)
        # this is a test to see if everything is working

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
