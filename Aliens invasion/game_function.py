import sys
import pygame

def check_events():
    """Обрабатывает нажатие клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Обновляет изображение на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()


    #Отображение последнего прорисованого экрана.
    pygame.display.flip()

