import time


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        interval_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"le temps d'execution est de {interval_time:0.6f} secondes")