class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Иннициализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False
        self.hight_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        