class GameStats():
    """
    Класс статистики игры, рекорды и т.д
    """
    
    def __init__(self, ai_settings):
        """
        Функция где мы задаем РЕКОРД и перезагружаем уровень.
        """
        self.ai_settings = ai_settings
        self.reset_stats()
        
        self.game_active = False
        
        self.high_score = 0
        
    def reset_stats(self):
        """
        Это перезагрузка уровня, обнуление результатов и переход на 1 уровень.
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
