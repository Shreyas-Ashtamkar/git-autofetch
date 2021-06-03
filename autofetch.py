from sched import scheduler
from time import time, sleep
from os import system

service = scheduler(time, sleep)

# while True:
service.enter(1, 1, system,("cd /mnt/Data_Drive/Codes/Python/useful-modules/git-src/batteryutils && git pull",) )
service.enter(1, 1, system,("pwd",) )
service.run()
