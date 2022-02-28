import time


class Timer:
    def __init__(self, logger=print, message="le temps d'execution est de {:0.6f} secondes"):
        self._start_time = None
        self.logger = logger
        self.message = message

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        interval_time = time.perf_counter() - self._start_time
        self._start_time = None
        #print(f"le temps d'execution est de {interval_time:0.6f} secondes")
        self.logger(self.message.format(interval_time))