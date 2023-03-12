from 显示元素.title import Title,Time
from 渲染器.moving_creater import *
import pygame,sys

class Control:
    def __init__(self,main_game):
        self.mouse_down = False
        self.settings = main_game.settings
        self.game = main_game
        #设置初始状态
        self.ifsetup = False
        self.ifwin = False
        self.select_step = 0

    def _init_1(self,main_game):
        self.display = main_game.display
        self.render = main_game.render
        self.music = main_game.music
        self.timer = main_game.timer
    
    def _init_2(self,main_game):
        self.history = main_game.history

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
                title = Title(self.game,'你不能移动空气',120)
                self.display.titles.add(title)
                #选择空塔不算步数
                self.select_step -= 1
        elif self.select_step == 2:
            #选择了目的地
            self.step_2 = order
            step = (self.step_1,self.step_2)
            result = tower.check_move(step)
            if result[0] == 'True':
                #通过移动检测，开始移动
                self.history.save(step)
                self._piece_move(step)
                tower.unselect(order)
                if tower.check():
                    #游戏完成
                    self._act_switch('inactive')
                    self.settle_accounts()
            else:
                #移动检测未通过
                title = Title(self.game,result[1],120)
                self.display.titles.add(title)
                tower.unselect(self.step_1)
                tower.unselect(self.step_2)
            self.select_step = 0
        else:
            raise Exception('发生啥事？')
    
    def _piece_move(self,step):
        tower = self.game.tower
        self._act_switch('inactive')
        moving = Moving_Curve(self.game,step)
        self.render.moving(moving)
        tower.move(step)
        self._act_switch('active')

    def undo(self):
        result = self.history.check('undo')
        if result[0] == True:
            #可以撤销
            step = self.history.undo()
            self._piece_move(step)
        else:
            title = Title(self.game,result[1],120)
            self.display.titles.add(title)

    def redo(self):
        result = self.history.check('redo')
        if result[0] == True:
            #可以重做
            step = self.history.redo()
            self._piece_move(step)
        else:
            title = Title(self.game,result[1],120)
            self.display.titles.add(title)

    def _act_switch(self,status):
        if status == 'active':
            for bt in self.display.control_bts:
                bt.active_switch('active')
            for chat_box in self.display.chat_boxes:
                chat_box.active_switch('active')
        else:
            for bt in self.display.control_bts:
                bt.active_switch('inactive')
            for chat_box in self.display.chat_boxes:
                chat_box.active_switch('inactive')

    #调用自动解决方案
    def auto_solve(self):
        self.tool_hud_out()
        self._act_switch('inactive')
        self.music.load('solve')
        self.music.play()
        self.history.clear()
        self.game.tower.auto_solve()
        self.ifwin = True
    
    #呼出侧栏
    def tool_hud_in(self):
        if self.ifsetup:
            self.timer.pause()
        self.music.pause()
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
        self.music.unpause()
        tool_hud = self.display.tool_hud
        tool_hud.active_switch('inactive')
        x,y = tool_hud.bg_rect.midleft
        tx,ty = self.render.screen.get_rect().midright
        coordinate = (x,y,tx,ty)
        moving = Moving_Straight(self.game,tool_hud,'midleft',coordinate)
        self.render.moving(moving)
        self.display.pause_bt.active_switch('active')
        if not self.ifwin:
            self._act_switch('active')
            if self.ifsetup:
                self.timer.unpause()

    #结算
    def settle_accounts(self):
        interval = round(self.timer.get(),1)
        self.ifwin = True
        step = self.history.step
        min_step = 2**self.game.n-1
        #步数部分的分
        if step == min_step:
            score_1 = 100
        elif step <= min_step*1.2:
            score_1 = 75
        elif step <= min_step*1.4:
            score_1 = 50
        else:
            score_1 = 25
        #时间部分的分
        ave_time = interval/step
        if ave_time <= 1:
            score_2 = 100
        elif ave_time <= 2:
            score_2 = 75
        elif ave_time <= 4:
            score_2 = 50
        else:
            score_2 = 25
        #最终结算
        score = score_1*0.4 + score_2*0.6
        if score == 100:
            self.music.load('best')
            rank = 'φ'
        elif score >= 75:
            self.music.load('better')
            rank = 'A'
        elif score >= 50:
            self.music.load('good')
            rank = 'B'
        else:
            self.music.load('notbad')
            rank = 'C'
        self.music.play()
        color = self.settings.get('color','rank',rank)
        self._settle_accounts_ani(interval,color,rank)

    def _settle_accounts_ani(self,interval,color,rank):
        title = Title(self.game,f'{rank} 你赢了 {rank}',-1,color)
        self.display.titles.add(title)
        self.display.make_time(interval)
        time = self.display.time
        x,y = time.rect.center
        tx,ty = self.render.screen.get_rect().center
        coordinate = (x,y,tx,ty-time.rect.height)
        moving = Moving_Straight(self.game,time,'center',coordinate)
        self.render.moving(moving)
        step_uhd = self.display.step
        x,y = step_uhd.rect.center
        coordinate = (x,y,tx,ty)
        moving = Moving_Straight(self.game,step_uhd,'center',coordinate)
        self.render.moving(moving)

    def restart(self):
        self.timer.reset()
        self.tool_hud_out()
        self.ifsetup = False
        self.history.clear()
        for i in self.display.control_bts.copy():
            self.display.control_bts.remove(i)
        for i in self.display.pieces.copy():
            self.display.pieces.remove(i)
        for i in self.display.titles.copy():
            self.display.titles.remove(i)