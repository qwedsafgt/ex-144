import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""#初始化button的属性
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50#设置按钮的尺寸
        self.button_color = (0, 255, 0)#设置按钮的背景色
        self.text_color = (255, 255, 255)#设置文本的颜色
        self.font = pygame.font.SysFont(None, 48)#指定用什么字体来渲染文本，none表示为默认字体，48设置字体颜色

        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)#我们创建表示一个按钮的rect对象
        self.rect.center = self.screen_rect.center#使按钮置于屏幕中央

        # The button message only needs to be prepped once.
        self.prep_msg(msg)#我们调用函数来处理这样的渲染

    def prep_msg(self, msg):#将msg渲染为图像，并使其在按钮上居中
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)#将msg中的文本转换为图像·
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center#让文本图像在按钮上居中

    def draw_button(self):#将按钮显示到屏幕上
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)#绘制矩形按钮
        self.screen.blit(self.msg_image, self.msg_image_rect)#绘制文本
