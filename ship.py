import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    Класс где мы реализовываем работу корабля.
    """

    def __init__(self, ai_settings, screen):
        """
        Функция иницирования работы корабля, его изображения, настроек.
        """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
 
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """
        Находим центр, для поставления корабля на центр экрана
        """
        self.center = self.screen_rect.centerx
        
    def update(self):
        """
        Реализация движения
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
 
        self.rect.centerx = self.center

    def blitme(self):
        """
        Отрисовка корабля
        """
        self.screen.blit(self.image, self.rect)
