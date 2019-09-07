class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""#初始化静态的设置
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1#以什么样的速度来加快游戏节奏
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()#初始化随游戏进行的属性

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5#设置了飞船的初始速度
        self.bullet_speed_factor = 3#设置了子弹的初始速度
        self.alien_speed_factor = 1#设置了外星人的初始速度

        # Scoring.
        self.alien_points = 50#每击中一个外星人的得分

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1#使外星人总是往右移

    def increase_speed(self):#提高速速的设置
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale#将每个元素的速度设置为原来的1。5倍
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)#外星人点数的提高
