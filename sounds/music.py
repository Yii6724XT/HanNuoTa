import pygame

class Music:
    def __init__(self):
        pass
    
    def load(self,name):
        pygame.mixer.music.load('sounds/'+name+'.ogg')

    def play(self):
        pygame.mixer.music.play(-1)
    
    def pause(self):
        pygame.mixer.music.pause()
    
    def unpause(self):
        pygame.mixer.music.unpause()
    
    def stop(self):
        pygame.mixer.music.stop()

# class Sounds:
#     def __init__(self,name):
#         self.sound = pygame.mixer.Sound('sounds/'+name+'.ogg')
    
#     def play(self):
#         self.sound.play()
        
if __name__ == '__main__':
    import time
    pygame.mixer.init()
    music = Music()
    music.load('good')
    music.play()
    time.sleep(5)
    music.pause()
    time.sleep(2)
    music.unpause()
    time.sleep(5)
    music.stop()
    input()