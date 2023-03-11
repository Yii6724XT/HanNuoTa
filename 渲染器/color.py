class Color:
    def __init__(self,main_game,seed):
        #获取设置
        self.settings = main_game.settings
        self.rgb_speed = self.settings.get('color','rgb_speed')
        self.seed = seed
        self.color = self._make_color()
        #设置默认状态
        self.default_seed = seed
        self.default_color = self.color
    
    #颜色生成器
    def _make_color(self):
        if self.seed >= 765:
            self.seed-=765
        if self.seed <= 255:
            r = 255-self.seed
            g = self.seed
            b = 0
        elif self.seed <= 510:
            t = self.seed-255
            r = 0
            g = 255-t
            b = t
        elif self.seed <= 764:
            t = self.seed-510
            r = t
            g = 0
            b = 255-t
        else:
            raise Exception('未知颜色')
        return(r,g,b)

    #RGB更新
    def rgb_update(self):
        self.seed+=self.rgb_speed
        self.color = self._make_color()
        return self.color
    
    #恢复默认
    def set_default(self):
        self.seed = self.default_seed
        self.color = self.default_color
        return self.color