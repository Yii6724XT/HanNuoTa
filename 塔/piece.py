import pygame
from pygame.sprite import Sprite

class Piece(Sprite):
    def __init__(self,main_game,tag,color):
        super().__init__()
        #获取设置
        self.settings = main_game.settings
        #初始化属性
        self.tag = tag
        self.screen = main_game.render.screen
        self.n = main_game.n
        self.color = color
        self.set_size()
        self.selected = False

    #设置大小
    def set_size(self):
        screen_rect = self.screen.get_rect()
        screen_width = screen_rect.width
        screen_height = screen_rect.height
        #计算高度
        if self.n <= 6:
            height = screen_height*(1/9)
        else:
            height = screen_height*(2/3)/self.n
        #计算宽度
        max_width = screen_width*(1/3)
        min_width = max_width*(1/4)
        if self.n > 1:
            difference = (max_width-min_width)/(self.n-1)
        else:
            difference = 0
        width = max_width-difference*(self.n-self.tag)
        #生成文字
        self.tag_image = self._make_tag_image(self.tag,height)
        #创建rect
        self.rect = pygame.Rect(0,0,width,height)
        self.tag_rect = self.tag_image.get_rect()

    #生成文字
    def _make_tag_image(self,tag,height):
        font_name = self.settings.get('font','font_name')
        font = pygame.font.SysFont(font_name,80)
        tag_color = self.settings.get('font','color')
        tag_image = font.render(str(tag),True,tag_color)
        #缩放到合适尺寸
        tag_image = pygame.transform.scale(tag_image,(height*0.6,height))
        return tag_image

    #移动位置
    def telepoint(self,anchor_point,tx,ty):
        if anchor_point == 'midbottom':
            self.rect.midbottom = (tx,ty)
            self.tag_rect.midbottom = (tx,ty)
        elif anchor_point == 'midtop':
            self.rect.midtop = (tx,ty)
            self.tag_rect.midtop = (tx,ty)
        else:
            raise Exception('无效锚点')

    #切换选中状态
    def select(self,status):
        if status == 'selected':
            self.selected = True
        else:
            self.selected = False

    #更新状态
    def update(self):
        if self.selected:
            color = self.color.rgb_update()
        else:
            color = self.color.set_default()
        self.screen.fill(color,self.rect)
        self.screen.blit(self.tag_image,self.tag_rect)