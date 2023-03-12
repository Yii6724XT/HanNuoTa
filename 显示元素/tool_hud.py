import pygame
from 显示元素.control_bts import *

class ToolHUD:
    def __init__(self,main_game):
        #获取设置
        self.settings = main_game.settings
        self.bg_color = self.settings.get('color','tool_hud')
        self.game = main_game
        #获取屏幕信息
        self.render = main_game.render
        self.screen = main_game.render.screen
        self.locations = main_game.render.locations
        #初始大小调整
        self.set_size()
        #初始化按钮
        self.bts = []
        self.bts.append(BackBt(self.game))
        #在这里加入其他功能按钮
        self.bts.append(ReBt(self.game))
        self.bts.append(AutoBt(self.game))
        #
        self.bts.append(QuitBt(self.game))
        for bt in self.bts:
            bt.active_switch('inactive')
        self._set_locations()

    #设置大小
    def set_size(self):
        screen_rect = self.screen.get_rect()
        screen_width = screen_rect.width
        screen_height = screen_rect.height
        bg_width = screen_width*(0.15)
        bg_height = screen_height
        self.bg_rect = pygame.Rect(0,0,bg_width,bg_height)
        self.bg_rect.midleft = screen_rect.midright

    #计算按钮位置
    def _set_locations(self):
        x = self.bg_rect.centerx
        bg_height = self.bg_rect.height
        bt_height = self.bts[0].rect.height
        ys = [bg_height*(1/9)+(bt_height*1.2)*n for n in range(6)]
        for i in range(len(self.bts)):
            bt = self.bts[i]
            bt.set_location(x,ys[i])

    def update(self):
        self.screen.fill(self.bg_color,self.bg_rect)
        for bt in self.bts:
            bt.update()
    
    def telepoint(self,anchor_point,tx,ty):
        if anchor_point == 'midright':
            self.bg_rect.midright = (tx,ty)
        elif anchor_point == 'midleft':
            self.bg_rect.midleft = (tx,ty)
        else:
            raise Exception('无效锚点')
        self._set_locations()

    def active_switch(self,status):
        if status == 'active':
            if self.game.control.ifsetup:
                if not self.game.control.ifwin:
                    for bt in self.bts:
                        bt.active_switch('active')
                else:
                    self.bts[0].active_switch('active')
                    self.bts[1].active_switch('active')
                    self.bts[-1].active_switch('active')
            else:
                #若游戏未完成设置，仅返回和退出可用
                self.bts[0].active_switch('active')
                self.bts[-1].active_switch('active')
        else:
            for bt in self.bts:
                bt.active_switch('inactive')