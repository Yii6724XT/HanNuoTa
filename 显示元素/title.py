import pygame
from pygame.sprite import Sprite

class Info(Sprite):
    def __init__(self,main_game,msg):
        super().__init__()
        self.settings = main_game.settings
        self.render = main_game.render
        self.screen = main_game.render.screen
        self.msg = msg
        self.set_size()
        self.set_location()

    def _make_msg_img(self):
        if self.screen.get_rect().height > 900:
            msg_size = self.settings.get('font','full_screen','pause')
        else:
            msg_size = self.settings.get('font','default','pause')
        font_name = self.settings.get('font','font_name')
        font = pygame.font.SysFont(font_name,msg_size)
        msg_color = self.settings.get('font','color')
        self.msg_image = font.render(self.msg,True,msg_color)

    def set_location(self):
        self.rect.center = self.render.locations['chat_box']['title']

    def set_size(self):
        self._make_msg_img()
        self.rect = self.msg_image.get_rect()

    def update(self,msg):
        if msg != self.msg:
            self.msg = msg
            self._make_msg_img()
        self.screen.blit(self.msg_image,self.rect)


class Title(Info):
    def __init__(self,main_game,msg,time,color=(0,0,0)):
        self.color = color
        super().__init__(main_game,msg)
        self.time = time
        self.group = main_game.display.titles
    
    def update(self):
        if self.time > 0:
            self.screen.blit(self.msg_image,self.rect)
            self.time -= 1
        elif self.time == 0:
            self.group.remove(self)
        elif self.time == -1:
            self.screen.blit(self.msg_image,self.rect)

    def set_location(self):
        x,y = self.render.locations['chat_box']['title']
        y -= self.rect.height
        self.rect.center = (x,y)
    
    def _make_msg_img(self):
        if self.screen.get_rect().height > 900:
            msg_size = self.settings.get('font','full_screen','pause')
        else:
            msg_size = self.settings.get('font','default','pause')
        font_name = self.settings.get('font','font_name')
        font = pygame.font.SysFont(font_name,msg_size)
        msg_color = self.color
        self.msg_image = font.render(self.msg,True,msg_color)

class Step(Info):
    def __init__(self,main_game):
        super().__init__(main_game,'步数：0')
        self.history = main_game.history

    def set_location(self):
        self.rect.midleft = self.render.locations['chat_box']['step']

    def update(self):
        new_msg = '步数：'+str(self.history.step)
        if new_msg != self.msg:
            self.msg = new_msg
            self._make_msg_img()
        self.screen.blit(self.msg_image,self.rect)
    
    def telepoint(self,anchor_point,tx,ty):
        self.rect.center = (tx,ty)

class Time(Info):
    def __init__(self,main_game,interval):
        h = interval//3600
        interval -= 3600*h
        m = interval//60
        s = interval-60*m
        print(f'用时：{h}h{m}m{s}s')
        super().__init__(main_game,f'用时{h}h{m}m{s}s')
    
    def set_location(self):
        self.rect.topleft = self.render.screen.get_rect().bottomright
    
    def update(self):
        self.screen.blit(self.msg_image,self.rect)
    
    def telepoint(self,anchor_point,tx,ty):
        self.rect.center = (tx,ty)