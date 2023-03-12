from 渲染器.moving_creater import Moving_Curve

class Logic:
    def __init__(self,main_game):
        self.settings = main_game.settings
        self.n = main_game.n
        self.render = main_game.render
        self.game = main_game

    #将片放到合适的位置
    def build(self,towers):
        self.locations = self.render.locations
        t = 0
        for T in towers:
            if len(T) > 0:
                tower = ('A','B','C')[t]
                piece = T[-1]
                x,y = self.locations['piece'][tower]
                piece.telepoint('midbottom',x,y)
                height = piece.rect.height
                for piece in T[-2::-1]:
                    y -= height
                    piece.telepoint('midbottom',x,y)
            t += 1

    #利用递归方法解决多层移动
    def _f(self,n,f_tower,t_tower,towers):
        if n == 1:
            step = (f_tower,t_tower)
            moving = Moving_Curve(self.game,step)
            self.render.moving(moving)
            towers.move(step)
        else:
            r_tower = 3-f_tower-t_tower
            self._f(n-1,f_tower,r_tower,towers)
            step = (f_tower,t_tower)
            moving = Moving_Curve(self.game,step)
            self.render.moving(moving)
            towers.move(step)
            self._f(n-1,r_tower,t_tower,towers)

    #自动解决方案
    def auto_solve(self,towers):
        n = self.n
        while True:
            if towers.check():
                break
            else:
                F = []
                E = []
                for T in towers.towers:
                    if len(T) == 0:
                        F.append(n+1)
                        E.append(n+1)
                    else:
                        first = T[0].tag
                        F.append(first)
                        for i in T[1:]:
                            if first+1 == i.tag:
                                first +=1
                            else:
                                break
                        E.append(first)
                hmin = n
                for e in range(3):
                    for f in range(3):
                        if e == f:
                            continue
                        else:
                            if E[e]+1 == F[f] and E[e] <= hmin:
                                hmin = E[e]
                                f_tower = e
                                t_tower = f
                                x = E[e]-F[e]+1
                self._f(x,f_tower,t_tower,towers)
    
'''    #利用非递归方法解决汉诺塔问题
    def auto_solve(self,towers):
        n = self.n
        self.towers = towers
        A,B,C = towers.towers
        #这个循环算法需要对奇偶进行讨论
        if n%2 == 0:
            tws = (A,B,C)
        else:
            tws = (A,C,B)
        #获取最小片的位置
        for top in range(3):
            try:
                if tws[top][0].tag == 1:
                    break
            except:
                #这是选到了空塔
                pass
        while True:
            #top_next是最小片所在塔的下一坐塔
            #用取模循环来获取下一坐塔的位置
            top_next = (top+1)%3
            #移动最小片
            self.submit_move(top,top_next)
            #使C塔填满的最后一片一定是最小的这片
            if len(C) == n:
                break
            else:
                order_1 = top
                order_2 = (top-1)%3
            try:
                tag_1 = tws[order_1][0].tag
            except:
                #如果遇到了空塔，它最上面一片按照
                #第n+1片来处理，以下同理
                tag_1 = n+1
            try:
                tag_2 = tws[order_2][0].tag
            except:
                tag_2 = n+1
            #判断移动方向，并移动
            if tag_1 < tag_2:
                self.submit_move(order_1,order_2)
            else:
                self.submit_move(order_2,order_1)
            #更新最小片的位置
            top = top_next

    def submit_move(self,f,t):
        step = (f,t)
        moving = Moving_Curve(self.game,step)
        self.render.moving(moving)
        self.towers.move(step)'''