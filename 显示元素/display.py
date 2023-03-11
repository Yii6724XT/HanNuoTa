from 显示元素.control_bts import *
from 显示元素.chat_boxes import *
from 显示元素.tool_hud import ToolHUD
import pygame

class Display:
    def __init__(self,main_game):
        self.game = main_game
        #生成需要渲染的群组
        self.elements = []
        #与对话框有关的部分
        self.chat_boxes = pygame.sprite.Group()
        self.elements.append(self.chat_boxes)
        #与控制按钮（ABC，撤销重做）有关的
        self.control_bts = pygame.sprite.Group()
        self.elements.append(self.control_bts)
        #与悬浮字幕有关的
        self.titles = pygame.sprite.Group()
        self.elements.append(self.titles)
        #与片有关的
        self.pieces = pygame.sprite.Group()
        self.elements.append(self.pieces)
        #暂停按钮
        self.pause_bt = PauseBt(self.game)
        self.elements.append(self.pause_bt)
        #与工具栏有关的
        self.tool_hud = ToolHUD(self.game)
        self.elements.append(self.tool_hud)
        #将生成的display交给render
        main_game.render.get_display(self)
    
    #生成控制按钮
    def make_control_bts(self):
        for tag in ('A','B','C'):
            button = ABC_Bt(self.game,tag)
            self.control_bts.add(button)
        self.control_bts.add(UndoBt(self.game))
        self.control_bts.add(RedoBt(self.game))

    def make_input_box(self):
        self.chat_boxes.add(Input_Box(self.game))