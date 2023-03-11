from 渲染器.calc_lacations import calc_locations
import pygame

class Render:
    def __init__(self,main_game):
        #获取设置
        self.settings = main_game.settings
        self.fps = self.settings.get('screen','max_fps')
        self.bg_color = self.settings.get('color','back_ground')
        full_screen = self.settings.get('screen','full_screen')
        self.control = main_game.control
        self.game = main_game
        #限制刷新率
        self.clock = pygame.time.Clock()
        #检查是否全屏
        if full_screen:
            #生成游戏画布
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.screen_width = self.screen.get_rect().width
            self.screen_height = self.screen.get_rect().height
        else:
            screen_size = self.settings.get('screen','size')
            self.screen_width,self.screen_height = screen_size
            #生成游戏画布
            self.screen = pygame.display.set_mode(screen_size)
        #计算元素位置
        self.locations=calc_locations(self.screen)
        #设置窗口标题
        pygame.display.set_caption('汉诺塔')
        
    #获得显示元素(由display提交)
    def get_display(self,display):
        self.display = display

    #更新所有元素
    def flash(self):
        self.clock.tick(self.fps)
        self.screen.fill(self.bg_color)
        #更新每个元素的状态
        for element in self.display.elements:
            element.update()
        pygame.display.flip()

    def moving(self,moving):
        while True:
            try:
                self.clock.tick(self.fps)
                self.control.update()
                ifquit = moving.update()
                self.flash()
                if ifquit:
                    break
            except Exception as err:
                print(err)
                moving.tp()
                self.game.tower.move(moving.step)
                raise Exception('solving_pause')