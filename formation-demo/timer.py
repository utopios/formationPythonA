import functools
import time


class Timer:
    def __init__(self, logger=print, message="le temps d'execution est de {:0.6f} secondes"):
        self.start_time = None
        self.logger = logger
        self.message = message

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        interval_time = time.perf_counter() - self.start_time
        self.start_time = None
        #print(f"le temps d'execution est de {interval_time:0.6f} secondes")
        self.logger(self.message.format(interval_time))


def decorator_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        start = time.perf_counter()
        value = func(*args, **kargs)
        interval_time = time.perf_counter() - start
        print(f"le temps d'execution est de {interval_time:0.6f} secondes")
        return value
    return wrapper