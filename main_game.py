from 渲染器.render import Render
from 设置.settings import Settings
from 控制.control import Control
from 显示元素.display import Display
from 塔.tower import Tower
import pygame,sys

class MainGame:
    def __init__(self):
        #初始化pygame
        pygame.init()
        #初始化设置
        self.settings = Settings()
        #初始化控制器
        self.control = Control(self)
        #初始化渲染器
        self.render = Render(self)
        #初始化显示元素
        self.display = Display(self)
        #默认层数
        self.n = self.settings.get('default_n')

    def setup(self):
        self.control._init_1(self.display,self.render)
        self.display.make_input_box()
        while True:
            try:
                self.control.update()
                self.render.flash()
                if self.control.ifsetup:
                    for input_box in self.display.chat_boxes.copy():
                        self.display.chat_boxes.remove(input_box)
                    break
            except Exception as err:
                reason = str(err)
                if reason == 'game_pause':
                    self.control.tool_hud_in()
                elif reason == 'exit_game':
                    sys.exit()
                else:
                    print(err)

    def run(self):
        #初始化塔
        self.tower = Tower(self)
        self.display.make_control_bts()
        while True:
            try:
                self.control.update()
                self.render.flash()
            except Exception as err:
                print(err)
                reason = str(err)
                if reason == 'game_pause':
                    self.control.tool_hud_in()
                elif reason == 'solving_pause':
                    self.control.tool_hud_in()
                elif reason == 'restart_game':
                    self.control.restart()
                    break
                elif reason == 'exit_game':
                    sys.exit()
                else:
                    print(err)

main_game = MainGame()
while True:
    main_game.setup()
    main_game.run()