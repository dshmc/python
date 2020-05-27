import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf 

def run_game():
    # Инициализация игры и создание объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height) )
    pygame.display.set_caption("Alien Invasion")
    
    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Созданиефлота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Создание пришельца
    #alien = Alien(ai_settings, screen)
    


# Запуск основного цикла игры

    while True:
# Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        
        ship.update()
        bullets.update()
        gf.update_bullets(aliens, bullets)   
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        #print(len(bullets))

run_game()
