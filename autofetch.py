from sched import scheduler
from time import time, sleep

from configs import DELAY
from projectfetcher import fetch

service = scheduler(time, sleep)

while True:
    service.enter(DELAY, 1, fetch)
    service.run()
