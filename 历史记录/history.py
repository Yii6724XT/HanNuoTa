class History:
    def __init__(self,main_game):
        #获取设置
        self.settings = main_game.settings
        self.max = self.settings.get('history','max_memory')
        #初始化
        self.clear()

    def clear(self):
        self.memory = []
        self.c = -1
        self.step = 0

    def save(self,step):
        self.c += 1
        rest = self.memory[self.c:]
        for i in rest:
            del self.memory[-1]
        self.memory.append(step)
        if len(self.memory) > self.max:
            del self.memory[0]
            self.c -= 1
        self.step += 1

    def check(self,type):
        if type == 'undo':
            if self.c > -1:
                return (True,)
            else:
                return (False,'你已经没有退路了')
        elif type == 'redo':
            if len(self.memory) > self.c+1:
                return (True,)
            else:
                return (False,'你已经无法再前进了')
    
    def undo(self):
        f = self.memory[self.c][1]
        t = self.memory[self.c][0]
        self.c -= 1
        self.step += 1
        return (f,t)
    
    def redo(self):
        self.c += 1
        f = self.memory[self.c][0]
        t = self.memory[self.c][1]
        self.step += 1
        return (f,t)