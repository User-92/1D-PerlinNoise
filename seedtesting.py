# SETUP---------------------------------------------------------
import pygame,noise,random,os,sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Perlin Noise Testing")
screen = pygame.display.set_mode((500,300),0,32)
# SETUP---------------------------------------------------------


#FUNCTIONS -----------------------------------------------------------------------------------
def gen_noise_rect(x,y,runcount):
    global height
    height = noise.pnoise2(x * 0.1,y * runcount, repeatx=999999999, repeaty=999999999) * 30
    return [x,y-height]


def gen_noise(runcount):
    noises = []
    for y in range(1):
        y += 100
        for x in range(500):
            rect = gen_noise_rect(x, y,runcount)
            noises.append(rect)
    return noises
#FUNCTIONS -----------------------------------------------------------------------------------

# variables
run_once = False # This isn't really needed, I just had it here to test
height = 1
seed = 0 # Input any seed here
hasnoise = False # used for checking if noise has been generated
while True:
    screen.fill((0,0,0)) #fill the screen with black

    if not run_once:
        noises = gen_noise(seed) # Generates the noise with the function defined above
        hasnoise=True
    if hasnoise:
        pygame.draw.lines(screen, [255, 255, 255], False, noises, 2) # Draws the lines for the noise

    # KEYS------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # KEYS------------------------------------------------
    pygame.display.update()
