import time

class MyTimer:
    def __init__(self):
        self.time_out = 300 #<- default 300 = 5 min
        self.elapsed = 0.0 # Abgelaufen
        self.running = False
        self.last_start_time = None

    def start(self):
        if not self.running:
            self.running = True
            self.last_start_time = time.time()

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed += time.time() - self.last_start_time

    def get_elapsed(self):
        elapsed = self.elapsed
        if self.running:
            elapsed += time.time() - self.last_start_time

        return int(elapsed)

    def get_current_sec(self):
        if self.running:
            current_sec = self.time_out - self.get_elapsed()
        return current_sec
