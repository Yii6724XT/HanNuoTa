import time

class Timer:
    def __init__(self):
        self.time = 0
        self.paused = False

    def start(self):
        self.sta = time.perf_counter()
    
    def pause(self):
        present = time.perf_counter()
        self.time += present-self.sta
        self.paused = True
    
    def unpause(self):
        self.sta = time.perf_counter()
        self.paused = False

    def get(self):
        if not self.paused:
            present = time.perf_counter()
            interval = present-self.sta + self.time
        else:
            interval = self.time
        return interval
    
    def reset(self):
        self.time = 0
        self.paused = False

if __name__ == '__main__':
    timer = Timer()
    timer.start()
    time.sleep(1)
    timer.pause()
    time.sleep(1)
    timer.unpause()
    time.sleep(1)
    print(timer.get())
