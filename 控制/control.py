from 显示元素.title import Title
from 渲染器.moving_creater import *
import pygame,sys

class Control:
    def __init__(self,main_game):
        self.mouse_down = False
        self.settings = main_game.settings
        self.game = main_game
        #设置初始状态
        self.ifsetup = False
        self.select_step = 0

    def _init_1(self,display,render):
        self.display = display
        self.render = render
    

    def update(self):
        #获取键盘状态
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        #获取鼠标状态
        mouse = pygame.mouse.get_pressed(num_buttons=3)
        self.mouse_down = mouse[0]
        #获取鼠标位置
        self.mouse_pos = pygame.mouse.get_pos()


    def confirm(self):
        if not self.ifsetup:
            self.ifsetup = True

    def cancel(self):
        if not self.ifsetup:
            self.game.n = self.settings.get('default_n') 

    def select(self,tag):
        self.select_step += 1
        order = {'A':0,'B':1,'C':2}[tag]
        tower = self.game.tower
        if self.select_step == 1:
            #检查是否选择空塔
            try:
                tower.select(order)
                self.step_1 = order
            except:
                title = Title(self.game,'你不能移动空气',60)
                self.display.chat_boxes.add(title)
                #选择空塔不算步数
                self.select_step -= 1
        elif self.select_step == 2:
            #选择了目的地
            self.step_2 = order
            step = (self.step_1,self.step_2)
            result = tower.check_move(step)
            if result[0] == 'True':
                #通过移动检测，开始移动
                self._act_switch('inactive')
                moving = Moving_Curve(self.game,step)
                self.render.moving(moving)
                tower.move(step)
                self._act_switch('active')
                tower.unselect(order)
                if tower.check():
                    #游戏完成
                    self._act_switch('inactive')
                    title = Title(self.game,'你赢了',60000)
                    self.display.titles.add(title)
            else:
                #移动检测未通过
                title = Title(self.game,result[1],60)
                self.display.titles.add(title)
                tower.unselect(self.step_1)
                tower.unselect(self.step_2)
            self.select_step = 0
        else:
            raise Exception('发生啥事？')

    def _act_switch(self,status):
        if status == 'active':
            for bt in self.display.control_bts:
                bt.active_switch('active')
            for chat_box in self.display.chat_boxes:
                chat_box.active_switch('active')
        else:
            for bt  in self.display.control_bts:
                bt.active_switch('inactive')
            for chat_box in self.display.chat_boxes:
                chat_box.active_switch('inactive')

    #调用自动解决方案
    def auto_solve(self):
        self.tool_hud_out()
        self._act_switch('inactive')
        self.game.tower.auto_solve()
    
    #呼出侧栏
    def tool_hud_in(self):
        self.display.pause_bt.active_switch('inactive')
        self._act_switch('inactive')
        tool_hud = self.display.tool_hud
        x,y = tool_hud.bg_rect.midright
        tx,ty = self.render.screen.get_rect().midright
        coordinate = (x,y,tx,ty)
        moving = Moving_Straight(self.game,tool_hud,'midright',coordinate)
        self.render.moving(moving)
        tool_hud.active_switch('active')
    
    #召回侧栏
    def tool_hud_out(self):
        tool_hud = self.display.tool_hud
        tool_hud.active_switch('inactive')
        x,y = tool_hud.bg_rect.midleft
        tx,ty = self.render.screen.get_rect().midright
        coordinate = (x,y,tx,ty)
        moving = Moving_Straight(self.game,tool_hud,'midleft',coordinate)
        self.render.moving(moving)
        self.display.pause_bt.active_switch('active')
        self._act_switch('active')
    
    def restart(self):
        self.tool_hud_out()
        self.ifsetup = False
        for i in self.display.control_bts.copy():
            self.display.control_bts.remove(i)
        for i in self.display.pieces.copy():
            self.display.pieces.remove(i)
        for i in self.display.titles.copy():
            self.display.titles.remove(i)