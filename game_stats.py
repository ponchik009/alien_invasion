# Строки 3,4 предотвращают проблему круговой зависимости
# При тайп-хинтинге
from __future__ import annotations
from typing import TYPE_CHECKING

import json

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
    
    # Рекорд, отображаемый в игре
    self.current_high_score = self._load_high_score()
    
  def reset_stats(self):
    """Инициализирует статистику, изменяющуюся в ходе игры"""
    self.ships_left = self.settings.ship_limit
    self.score = 0
    self.level = 1
    
  def save_high_score(self):    
    with open("data/high_score.json", 'w') as f:
      json.dump(self.current_high_score, f)
    
  def _load_high_score(self):
    """Загружает рекорд из файла"""
    try:
      with open("data/high_score.json", 'r') as f:
        high_score = int(json.load(f))
    except FileNotFoundError:
      high_score = 0
    except Exception:
      high_score = 0
    
    return high_score
    