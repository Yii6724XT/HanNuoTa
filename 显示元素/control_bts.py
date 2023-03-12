from 显示元素.button import Button

#ABC按钮（tag为'A','B','C'）
class ABC_Bt(Button):
    def __init__(self,main_game,tag):
        super().__init__(main_game,tag,'large')
        self.control = main_game.control
        self.tag = tag
        self.set_location()


    def set_location(self):
        self.center = self.locations['ABC_bt'][self.tag]
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.control.select(self.tag)


class UndoBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'撤消','small')
        self.set_location()
    
    def set_location(self):
        self.center = self.locations['left_hud']['undo']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.control.undo()


class RedoBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'重做','small')
        self.set_location()
    
    def set_location(self):
        self.center = self.locations['left_hud']['redo']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.control.redo()


class PauseBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'暂停','small')
        self.set_location()

    def set_location(self):
        self.center = self.locations['right_hud']['pause']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        raise Exception('game_pause')


class BackBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'回到游戏','medium')

    def set_location(self,x,y):
        self.rect.center = (x,y)
        self.msg_rect.center = (x,y)

    def _function(self):
        self.control.tool_hud_out()

class QuitBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'退出游戏','medium')

    def set_location(self,x,y):
        self.rect.center = (x,y)
        self.msg_rect.center = (x,y)

    def _function(self):
        raise Exception('exit_game')

class ReBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'重玩游戏','medium')

    def set_location(self,x,y):
        self.rect.center = (x,y)
        self.msg_rect.center = (x,y)

    def _function(self):
        raise Exception('restart_game')

class AutoBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'自动解决','medium')

    def set_location(self,x,y):
        self.rect.center = (x,y)
        self.msg_rect.center = (x,y)

    def _function(self):
        self.control.auto_solve()