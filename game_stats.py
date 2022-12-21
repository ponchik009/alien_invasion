# Строки 3,4 предотвращают проблему круговой зависимости
# При тайп-хинтинге
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class GameStats():
  """Отслеживание статистики для игры Alien Inavsion"""
  
  def __init__(self, ai_game: AlienInvasion):
    """Инициализирует статистику"""
    self.settings = ai_game.settings
    self.reset_stats()
    
    # Игра Alien Invasion запускается в неактивном состоянии
    self.game_active = False
    
    # Рекорд, который не сбрасывается
    self.high_score = 0
    
  def reset_stats(self):
    """Инициализирует статистику, изменяющуюся в ходе игры"""
    self.ships_left = self.settings.ship_limit
    self.score = 0
    self.level = 1