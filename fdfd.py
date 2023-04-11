import pygame
import sys

pygame.init()

player_x = 800
player_y = 0
player_color = (0, 204, 102)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) # экран
pygame.display.set_caption("Моя программа")

player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player = pygame.Rect((player_x, player_y, player_width, player_height))


while True: # главный цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                player.x += 20
            if event.key == pygame.K_LEFT:
                player.x -= 20
            if event.key == pygame.K_DOWN:
                player.y += 20
            if event.key == pygame.K_UP:
                player.y -= 20
            if event.key == pygame.K_SPACE:
                player.y -= 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 1
    if keys[pygame.K_DOWN]:
        player.y += 1
    if keys[pygame.K_RIGHT]:
       player.x += 1
    if keys[pygame.K_LEFT]:
        player.x -= 1



    # отрисовка
    screen.fill((0, 0, 0))                                               
    pygame.draw.rect(screen, player_color, player)
    pygame.display.flip()