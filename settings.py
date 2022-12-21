class Settings:
  """Класс для хранения всех настроек игры"""
  
  def __init__(self) -> None:
    """Инициализирует статические настройки игры"""
    # Параметры экрана
    self.is_fullscreen = False
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)
    
    # Настройки корабля
    self.ship_limit = 3
    
    # Параметры снаряда
    self.bullet_width = 3000
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 300000
    
    # Настройки пришельцев
    self.fleet_drop_speed = 50
    
    # Темп ускорения игры
    self.speedup_scale = 1.1
    # Темп роста стоимости пришельцев
    self.score_scale = 1.5
    
    self.initialize_dynamic_settings()
    
  def initialize_dynamic_settings(self):
    """Инициализирует настройки, изменяющиеся в ходе игры"""
    self.ship_speed = 0.5
    self.bullet_speed = 1
    self.alien_speed = 0.3
    
    # 1 - вправо, -1 - влево
    self.fleet_direction = 1
    
    # Подсчёт очков
    self.alien_points = 50
    
  def increase_speed(self):
    """Ускоряет игру"""
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale
    
    self.alien_points *= self.score_scale