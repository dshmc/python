import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf 
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    # Создание пришельца
    #alien = Alien(ai_settings, screen)
    


# Запуск основного цикла игры

    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)   
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        

run_game()
