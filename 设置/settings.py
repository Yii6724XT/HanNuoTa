class Settings:
    def __init__(self):
        self.settings={
                       'default_n':6,
                       'screen':
                            {
                             'size':(1600,900),
                             'full_screen':False,
                             'max_fps':120
                            },
                        'color':
                            {
                             'back_ground':(26,148,220),
                             'rgb_speed':10,
                             'button_seed':200,
                             'button_gray':(127,127,127),
                             'tool_hud':(14,84,155)
                            },
                        'font':
                            {
                             'font_name':'dengxian',
                             'full_screen':{'ABC':80,'tool':30,'pause':60},
                             'default':{'ABC':65,'tool':25,'pause':50},
                             'color':(0,0,0)
                            },
                        'animation':
                            {
                             'enabled':True,
                             'speed':30,
                             'speed_s':10
                            }
                      }
    #查找设置
    def get(self,*key):
        value = self.settings[key[0]]
        for key_0 in key[1:]:
            value = value[key_0]
        return value

if __name__ == '__main__':
    settings = Settings()