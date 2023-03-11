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
        self.msg = msg
        self._make_msg_img()
        self.screen.blit(self.msg_image,self.rect)


class Title(Info):
    def __init__(self,main_game,msg,time):
        super().__init__(main_game,msg)
        self.time = time
        self.group = main_game.display.titles
    
    def update(self):
        if self.time > 0:
            self.screen.blit(self.msg_image,self.rect)
            self.time -= 1
        elif self.time == 0:
            self.group.remove(self)

    def set_location(self):
        x,y = self.render.locations['chat_box']['title']
        y -= self.rect.height
        self.rect.center = (x,y)