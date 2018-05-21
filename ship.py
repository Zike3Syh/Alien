import  pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化飞船图像并设置它的初始位置'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞图像并获得其外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部正中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx

    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更新飞船的center值而非rect值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center对象更新rectd对象
        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)