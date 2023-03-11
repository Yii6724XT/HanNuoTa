from 渲染器.color import Color
from 塔.logic import Logic
from 塔.piece import Piece

class Tower:
    def __init__(self,main_game):
        self.display_group = main_game.display.pieces
        self.n = main_game.n
        self.A = []
        self.B = []
        self.C = []
        self.towers = (self.A,self.B,self.C)
        for tag in range(1,self.n+1):
            seed = int((tag/self.n)*764)
            color = Color(main_game,seed)
            piece = Piece(main_game,tag,color)
            self.A.append(piece)
            self.display_group.add(piece)
        self.logic = Logic(main_game)
        self.logic.build(self.towers)

    def select(self,order):
        self.towers[order][0].select('selected')

    def unselect(self,order):
        self.towers[order][0].select('unselected')

    def check_move(self,step):
        f_tower,t_tower = step
        f_tag = self.towers[f_tower][0].tag
        try:
            t_tag = self.towers[t_tower][0].tag
        except:
            t_tag = self.n+1
        if f_tower == t_tower:
            self.towers[f_tower][0].select('unselected')
            return ('False','你搁这搁这呢！')
        else:
            if f_tag < t_tag:
                return ('True',)
            else:
                return ('False','你只能把小的片放到大的上')
    
    def move(self,step):
        f_tower,t_tower = step
        x = self.towers[f_tower].pop(0)
        self.towers[t_tower].insert(0,x)

    def check(self):
        if len(self.C) == self.n:
            return True
        else:
            return False

    def auto_solve(self):
        self.logic.auto_solve(self)