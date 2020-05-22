import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf 

def run_game():
    #Инициализация игры и создание объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height) )
    pygame.display.set_caption("Alien Invasion")
    
    #Создание корабля
    ship = Ship(ai_settings, screen)

    #Создание группы для хранения пуль.
    bullets = Group()
    


#Запуск основного цикла игры

    while True:
# Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
