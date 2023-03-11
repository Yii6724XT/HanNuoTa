from 显示元素.button import Button

class ConfirmBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'确定','large')
        self.control = main_game.control
        self.set_location()

    def set_location(self):
        self.center = self.locations['chat_box']['confirm_bt']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.control.confirm()

class CancelBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'取消','large')
        self.control = main_game.control
        self.set_location()

    def set_location(self):
        self.center = self.locations['chat_box']['cancel_bt']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.control.cancel()

class AddBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'增加','small')
        self.game = main_game
        self.set_location()

    def set_location(self):
        self.center = self.locations['chat_box']['add_bt']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.game.n += 1

class ReduceBt(Button):
    def __init__(self,main_game):
        super().__init__(main_game,'减少','small')
        self.game = main_game
        self.set_location()

    def set_location(self):
        self.center = self.locations['chat_box']['reduce_bt']
        self.rect.center = self.center
        self.msg_rect.center = self.center

    def _function(self):
        self.game.n -= 1