import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Класс где мы будем реализовывать работу пришельца, вырисовывать его, искать его координаты,
    делать проверки, реализовывать его движение и задавать поведение
    """

    def __init__(self, ai_settings, screen):
        """
        Здесь мы иницируем функцию пришельцев, задаем пришельцам вид, настройки, ищем координаты
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        
    def check_edges(self):
        """
        Проверка на выход за экран, в случае когда
        пришелец выходит за экран, мы узнаем это
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """
        Функция с движением пришельцев
        """
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Отрисовка пришельцев"""
        self.screen.blit(self.image, self.rect)
