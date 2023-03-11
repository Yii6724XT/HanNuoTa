
#记得在调用tower.move()前使用
class Moving_Curve():
    def __init__(self,main_game,step):
        #获取设置
        self.settings = main_game.settings
        self.screen_width = main_game.render.screen_width
        self.locations = main_game.render.locations
        self.animation_enabled = self.settings.get('animation','enabled')
        self.speed = self.settings.get('animation','speed')
        #获取实例
        towers = main_game.tower.towers
        f_tower,t_tower = step
        #储存要绘制的实例
        self.step = step
        self.piece = towers[f_tower][0]
        #计算坐标
        try:
            piece_1 = towers[t_tower][0]
            self.tx,self.ty = piece_1.rect.midtop
            self.ty -= piece_1.rect.height
        except:
            tag = ('A','B','C')[t_tower]
            self.tx,self.ty = self.locations['piece'][tag]
            self.ty -= self.piece.rect.height
        #动画是否启用
        if self.animation_enabled:
            self.x,self.y = self.piece.rect.midtop
            self.a,self.m = self._calculate_curve(
                                self.x,self.y,self.tx,self.ty)
            if self.x > self.tx:
                #目的地在起点左侧，速度设为负
                self.speed = 0-self.speed
                self.direction = 'left'
            else:
                self.direction = 'right'
            #若位移较大，调快速度
            if abs(self.x - self.tx) > self.screen_width*(1/3)+10:
                self.speed *= 2

    def update(self):
        if self.animation_enabled:
            self.x += self.speed
            if self.direction == 'right':
                if self.x >= self.tx:
                    self.piece.telepoint('midtop',self.tx,self.ty)
                    return True
                else:
                    self.y = self.a*(self.x-self.m)**2
                    self.piece.telepoint('midtop',self.x,self.y)
                    return False
            elif self.direction == 'left':
                if self.x <= self.tx:
                    self.piece.telepoint('midtop',self.tx,self.ty)
                    return True
                else:
                    self.y = self.a*(self.x-self.m)**2
                    self.piece.telepoint('midtop',self.x,self.y)
                    return False
        else:
            self.piece.telepoint('midtop',self.tx,self.ty)
            return True

    def _calculate_curve(self,x_1,y_1,x_2,y_2):
        bi = (y_1/y_2)**0.5
        m = (x_1+bi*x_2)/(bi+1)
        a = y_1/(x_1-m)**2
        return (a,m)
    
    def tp(self):
        self.piece.telepoint('midtop',self.tx,self.ty)

import math

class Moving_Straight:
    def __init__(self,main_game,element,anchor_point,coordinate):
        speed = main_game.settings.get('animation','speed_s')
        self.animation_enabled = main_game.settings.get('animation','enabled')
        self.x,self.y = coordinate[0:2]
        self.tx,self.ty = coordinate[2:4]
        #储存移动对象
        self.element = element
        self.anchor_point = anchor_point
        #检测斜率是否存在
        if self.tx != self.x:
            self.vertical = False
            self.k = (self.ty-self.y)/(self.tx-self.x)
            self.A = (self.tx-self.x)/2
        else:
            self.vertical = True
            self.A = (self.ty - self.y)/2
        #计算动画共需播放多少帧
        self.f = 0
        self.frames = abs(self.tx-self.x)/speed
        #移动方向
        if self.vertical:
            if self.y < self.ty:
                self.direction = '+'
            else:
                self.direction = '-'
        else:
            if self.x < self.tx:
                self.direction = '+'
            else:
                self.direction = '-'

    def update(self):
        if self.animation_enabled:
            reach = False
            self.f += 1
            if not self.vertical:
                x = self.A*(math.sin((self.f/self.frames)*math.pi-math.pi/2)+1)+self.x
                if self.direction == '+':
                    if x+1 >= self.tx:
                        reach = True
                else:
                    if x-1 <= self.tx:
                        reach = True
                y = self.k*(x-self.tx)+self.ty
            else:
                x = self.x
                y = self.A*(math.sin((self.f/self.frames)*math.pi-math.pi/2)+1)+self.y
                if self.direction == '+':
                    if self.y+1 >= self.ty:
                        reach = True
                else:
                    if self.y-1 <= self.ty:
                        reach = True
            if reach:
                self.element.telepoint(self.anchor_point,self.tx,self.ty)
                return True
            else:
                self.element.telepoint(self.anchor_point,x,y)
                return False
        else:
            self.element.telepoint(self.anchor_point,self.tx,self.ty)
            return True
        