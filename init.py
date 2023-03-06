#pylint: disable = E1101
import sys
import os
import pygame
import random


pygame.init()
pygame.mixer.init()

speed = [5, 5]
sus = pygame.mixer.Sound("assets/sus_effect.wav")
clock = pygame.time.Clock()
screen_wide = width, height = (1920, 1080)
display = pygame.display.set_mode(screen_wide)
dvd_path = os.path.join('assets', '7.png')
dvd_img = pygame.image.load(dvd_path)
dvd_surf = pygame.Surface.convert_alpha(dvd_img)
dvd = pygame.transform.scale(dvd_surf, (313, 142))
ballrect = dvd.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        dvd_surf = pygame.Surface.convert_alpha(
            pygame.image.load(f"./assets/{random.randint(0, 7)}.png"))
        dvd = pygame.transform.scale(dvd_surf, (313, 142))


    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        dvd_surf = pygame.Surface.convert_alpha(
            pygame.image.load(f"./assets/{random.randint(0, 7)}.png"))
        dvd = pygame.transform.scale(dvd_surf, (313, 142))
        display.blit(pygame.image.load("assets/jackpot.png"), (0,0))

    if ((ballrect.top == 0 and ballrect.left == 0) or
    (ballrect.bottom == height and ballrect.left == 0) or
    (ballrect.top == 0 and ballrect.right == width) or
    (ballrect.bottom == height and ballrect.left == width)):
        print("SHOT TIME")
        pygame.mixer.Sound.play(sus)

    display.blit(pygame.image.load("assets/bg.png"), (0,0))
    display.blit(dvd, ballrect)
    pygame.display.flip()
    clock.tick(30)
