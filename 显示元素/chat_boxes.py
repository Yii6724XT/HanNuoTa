from 显示元素.title import Info,Title
from 显示元素.chat_bts import *
import pygame
from pygame.sprite import Sprite

class Input_Box(Sprite):
    def __init__(self,main_game):
        super().__init__()
        self.settings = main_game.settings
        self.control = main_game.control
        self.screen = main_game.render.screen
        self.game = main_game
        self.display = main_game.display
        #初始化按钮群组
        self.bt_group = pygame.sprite.Group()
        self.bt_group.add(ConfirmBt(main_game))
        self.bt_group.add(CancelBt(main_game))
        self.bt_group.add(AddBt(main_game))
        self.bt_group.add(ReduceBt(main_game))
        #显示信息
        self.info = Info(main_game,f'层数：{self.game.n}')
    
    def update(self):
        #按钮群组
        self.bt_group.update()
        if self.game.n <= 0:
            self.game.n = self.settings.get('default_n')
            title = Title(self.game,'不能是负数哦，亲。',60)
            self.display.titles.add(title)
        self.info.update(f'层数：{self.game.n}')
    
    def active_switch(self,status):
        if status == 'active':
            for bt in self.bt_group:
                bt.active_switch('active')
        else:
            for bt in self.bt_group:
                bt.active_switch('inactive')