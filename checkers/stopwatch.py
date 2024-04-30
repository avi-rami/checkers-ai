import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        self.start_time = None
        self.running = False

    def get_elapsed_time(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            return elapsed_time
        return 0


    def get_elapsed_time_str(self):
        elapsed_time = self.get_elapsed_time()
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        formatted_time = f"{minutes:02}:{seconds:02}"  # Formatting the time into a string
        return formatted_time
