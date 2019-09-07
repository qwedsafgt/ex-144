import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():#我们用这个类来显示的分
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):#初始化显示得分涉及的属性
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)#显示得分的字体设置
        self.font = pygame.font.SysFont(None, 48)#实例化一个字体对象

        # Prepare the initial score images.
        self.prep_score()#将要显示的文本转换为图像
        self.prep_high_score()
        self.prep_level()#显示当前等级
        self.prep_ships()#显示还剩下多少飞船

    def prep_score(self):#将得分换成一幅渲染的图像
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))#把圆整到最近的等整数倍
        score_str = "{:,}".format(rounded_score)#我们首先将数字值转化为字符串
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)#将字符串传递给font，使其转换为图像

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20#使这个得分始终与屏幕保持20像素的距离
        self.score_rect.top = 20

    def prep_high_score(self):#将最高得分转换为渲染的对象
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))#我们将最高得分元整到最近的10的整数倍
        high_score_str = "{:,}".format(high_score)#并且添加了用逗号表示的千分位分隔符
        self.high_score_image = self.font.render(high_score_str, True,#然后我们把最高得分生成一幅图像，并使其水平居中，

            self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx#水平居中
        self.high_score_rect.top = self.score_rect.top#将top属性设置为当前得分的top属性

    def prep_level(self):#将等级转化为渲染的图像
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)#根据储存的值创建一幅图像

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right#设置为和得分图像垂直
        self.level_rect.top = self.score_rect.bottom + 10#设置为比得分图像bottom像素大10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()#储存飞船实例
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)#创建一艘飞船
            ship.rect.x = 10 + ship_number * ship.rect.width#让整个飞船编组位于屏幕左边
            ship.rect.y = 10#使得每一艘飞船都与得分图像对齐
            self.ships.add(ship)#我们把飞船添加到编组中去

    def show_score(self):
        """Draw score to the screen."""#在屏幕上显示当前得分和最高得分
        self.screen.blit(self.score_image, self.score_rect)#显示当前得分
        self.screen.blit(self.high_score_image, self.high_score_rect)#显示最高得分
        self.screen.blit(self.level_image, self.level_rect)#显示等级
        # Draw ships.
        self.ships.draw(self.screen)#在屏幕上绘制飞船
