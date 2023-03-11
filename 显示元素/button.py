from 渲染器.color import Color
import pygame
from pygame.sprite import Sprite

class Button(Sprite):
    def __init__(self,main_game,msg,size):
        #初始化精灵继承
        super().__init__()
        #获取设置
        self.settings = main_game.settings
        self.control = main_game.control
        self.screen = main_game.render.screen
        self.locations = main_game.render.locations
        self.msg = msg
        #初始化颜色
        self.gray_color = self.settings.get('color','button_gray')
        seed = self.settings.get('color','button_seed')
        self.color = Color(main_game,seed)
        #初始化大小
        self.size = size
        self.set_size()
        self.active = True

    #切换活动状态
    def active_switch(self,status):
        if status == 'active':
            self.active = True
        else:
            self.active = False

    #根据预设的'large','medium','small'和屏幕分辨率设置大小
    def set_size(self):
        #计算按钮大小
        screen_rect = self.screen.get_rect()
        screen_width = screen_rect.width
        screen_height = screen_rect.height
        if screen_height>900:
            screen_size = 'full_screen'
        else:
            screen_size = 'default'
        if self.size == 'large':
            width = screen_width*(1/8)
            height = screen_height*(1/15)
            msg_size = self.settings.get('font',screen_size,'ABC')
        elif self.size == 'medium':
            width = screen_width*(1/8)
            height = screen_height*(1/15)
            msg_size = self.settings.get('font',screen_size,'pause')
        elif self.size == 'small':
            width = screen_width*(2/64)
            height = screen_height*(1/18)
            msg_size = self.settings.get('font',screen_size,'tool')
        else:
            raise Exception('未定义的按钮大小')
        self.rect = pygame.Rect(0,0,width,height)
        #设置字体
        self.msg_image = self._make_msg_image(msg_size)
        self.msg_rect = self.msg_image.get_rect()
        #flag
        self.flag = True

    #创建按钮文字
    def _make_msg_image(self,msg_size):
        font_name = self.settings.get('font','font_name')
        font = pygame.font.SysFont(font_name,msg_size)
        msg_color = self.settings.get('font','color')
        msg_image = font.render(self.msg,True,msg_color)
        return msg_image

    #设置按钮位置
    def set_location(self):
        #默认按钮手动放置位置
        center = self.screen.get_rect().center
        self.rect.center = center
        self.msg_rect.center = self.rect.center

    #点击时动作
    def _function(self):
        pass

    #更新按钮状态
    def update(self):
        if self.active:
            mouse_pose = self.control.mouse_pos
            if self.rect.collidepoint(mouse_pose):
                mouse_down = self.control.mouse_down
                if not mouse_down:
                    self.flag = True
                if mouse_down and self.flag:
                    self.flag = False
                    #点击按钮时设置为当前颜色，即静止
                    color = self.color.color
                    self._function()
                else:
                    color = self.color.rgb_update()
            else:
                color = self.color.set_default()
        else:
            color = self.gray_color
        #在屏幕上绘制按钮
        self.screen.fill(color,self.rect)
        self.screen.blit(self.msg_image,self.msg_rect)