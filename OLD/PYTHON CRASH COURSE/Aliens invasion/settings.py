class Settings():
    #Класс для хранения всех настроек игры

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Параметры пули
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60 ,60, 60
        self.bullet_allowed = 3

        # Настройка пришельцев
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево.
        self.fleet_direction = 1


        #Темп игры 
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Инициализирует настройки, изменяющиеся в ходе игры.
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        
        # fleet_direction = 1 обозначает движение вправо, а -1 влево.
        self.fleet_direction = 1
        self.allien_points = 50
    
    def increase_speed(self):
        """ Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale
        self.allien_points = int(self.allien_points * self.score_scale)
                

        
        
