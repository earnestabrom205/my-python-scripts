import threading


class Racer(threading.Thread):
    def __init__(self, name, start_signal):
        threading.Thread.__init__(self, name=name)
        self.start_signal = start_signal

    def run(self):
        self.start_signal.wait()
        print(f"I, {self.name}, got to the goal!")


class Race:
    
    def __init__(self, racer_names):
        self.start_signal = threading.Event()
        self.racers = [Racer(name, self.start_signal) for name in racer_names]
        for racer in self.racers:
            racer.start()

    def start(self):
        self.start_signal.set()


def __main__():
    race = Race(["rabbit", "turtle", "cheetah", "monkey", "cow", "horse", "tiger", "lion"])
    race.start()



__main__()
