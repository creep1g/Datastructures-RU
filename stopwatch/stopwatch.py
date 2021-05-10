'''Stopwatch class'''
import time


class StopWatch:

    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.delta_time = 0
        self.last_lap_time = 0
        self.pause_start = 0
        self.pause_delta = 0
        self.paused = False
        self.lap_pause_duration = 0
        self.history = []

    def startTimer(self):
        self.start_time = time.perf_counter()
        self.last_lap_time = self.start_time
        self.pause_duration = 0
        self.lap_pause_duration = 0

    def getDuration(self):
        return self.delta_time

    def getTimeFromStart(self):
        self.delta_time = ((time.perf_counter() - self.start_time -
                            self.pause_delta) * 1000)

    def getLapTime(self):
        if self.paused:
            return "PAUSED"
        else:
            current_time = time.perf_counter()
            return_time = current_time - self.last_lap_time
            self.last_lap_time = current_time
            self.lap_pause_duration = 0
            return int((return_time)*1000)

    def stopTimer(self):
        self.delta_time = int((time.perf_counter() - self.start_time -
                               self.pause_delta) * 1000)
        self.history.append([f'{self.start_time:9.1f}',
                             (int(self.pause_delta * 1000)),
                             self.delta_time])

    def pauseTimer(self):
        self.paused = True
        self.pause_start = time.perf_counter()

    def unPauseTimer(self):
        self.paused = False
        self.pause_delta += time.perf_counter() - self.pause_start

    def getPausedDuration(self):
        return int(self.pause_delta * 1000)

    def getTimerHistory(self):
        count = 0
        print("{:<8} | {:<15} | {:<15} | {:<15}".format("Nr", "Start Time",
                                                        "Pause Duration",
                                                        "Total Time"))
        for instance in self.history:
            print("{:<8} | {:<15} | {:<15} | {:<15}".format(count, instance[0],
                                                            instance[1],
                                                            instance[2]))


if __name__ == "__main__":

    timer = StopWatch()

    timer.startTimer()
    n = 0
    pauses = [2, 5, 9, 23, 142, 42]
    for i in range(98921):
        if i in pauses:
            timer.pauseTimer()
            time.sleep(0.002)
        print("Lap TIME BABY: {} ms".format(timer.getLapTime()))
        if i in pauses:
            timer.unPauseTimer()

    timer.stopTimer()
    print("Total time paused: {} ms".format(timer.getPausedDuration()))
    print("Total time: {} ms".format(timer.getDuration()))
    timer.getTimerHistory()
