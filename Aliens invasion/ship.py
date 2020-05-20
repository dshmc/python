import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ Рисует корабль в текущей позиции. """

        self.screen.blit(self.image, self.rect) 