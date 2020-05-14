import sys
import pygame

def run_game():
    #Инициализация игры и создание объекта экрана
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")


#Запуск основного цикла игры

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            pygame.display.flip()

run_game()
