import pygame
import Character
import Enemy
import Treasure
from wall import Wall
pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)


pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

fon = pygame.image.load("background3.png")
fon = pygame.transform.scale(fon, (800,500))

pacman = Character.Character(105, 80, 50, 50, 5, "hero.png")
cyborg = Enemy.Enemy(280, 380, 50, 50, 5, "cyborg.png", 100, 100, 400, 400)
treasure = Treasure.Treasure(100, 200, 50, 50,  "treasure.png")

game = True

walls = []
walls. append(Wall(195, 60, 160, 5, (255, 255, 0)))
walls. append(Wall(295, 450, 120, 5, (255, 255, 0)))
walls. append(Wall(415, 295, 120, 5, (255, 255, 0)))
walls. append(Wall(415, 295, 5, 105, (255, 255, 0)))





while game:



    window.fill((123, 123, 123))
    window.blit(fon, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)


        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    pacman.move()
    pacman.render(window)
    cyborg.move()
    cyborg.render(window)
    treasure.render(window)
    for wall in walls:
        wall.render(window)

    pygame.display.flip()
    fps.tick(60)

