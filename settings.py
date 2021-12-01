class Settings():
    """
    Класс с настройками игры
    """

    def __init__(self):
        """
        Натсройки экрана, корабля, пуль, пришельцев и т.д.
        """
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 1
        self.bullet_width = 1
        self.bullet_height = 47
        self.bullet_color = 255, 230, 0
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Задаем динамические факторы, которые будут обновляться с увеличением сложности.
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        self.alien_points = 50

        self.fleet_direction = 1
        
    def increase_speed(self):
        """
        Увеличение сложности
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)