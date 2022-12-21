# Строки 3,4 предотвращают проблему круговой зависимости
# При тайп-хинтинге
from __future__ import annotations
from typing import TYPE_CHECKING

import pygame.font
from pygame import Rect

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button():
  """Класс реализует кнопку"""
  
  def __init__(self, ai_game: AlienInvasion, msg: str):
    """Инициализирует атрибуты кнопки"""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    
    # Назначение размером и свойств кнопок
    self.width, self.height = 200, 50
    self.button_color = (0, 255, 0)
    self.text_color = (255, 255, 255)
    self.font = pygame.font.SysFont(None, 48)
    
    # Построение объекта rect кнопки и выравнивание по центру экрана
    self.rect = Rect(0, 0, self.width, self.height)
    self.rect.center = self.screen_rect.center
    
    # Сообщение кнопки создаётся только один раз
    self._prep_msg(msg)
    
  def _prep_msg(self, msg: str):
    """Преобразует msg в прямогульник и выравнивает текст по центру"""
    self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
    self.msg_image_rect = self.msg_image.get_rect()
    self.msg_image_rect.center = self.rect.center
    
  def draw_button(self):
    """Отображение пустой кнопки и вывод сообщения"""
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.msg_image, self.msg_image_rect)