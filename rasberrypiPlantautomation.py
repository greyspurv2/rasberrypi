import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import Rpi.GPIO as io


def __init__(self, watercycle, lightcycle, pumpcycle):
    self.watercycle = watercycle
    self.pumpcycle = pumpcycle
    self.lightcycle = lightcycle


#water cycle
while True:
start:
datetime.date(now) = True



#pump time (seconds) Adjust according to pump intensity and diameter of tubeing
    if True:
    pump.pump = time.time() + 5
    if
    time.time() < pump:

    pump_Start
    else
    pump_Stop
            dt = datetime.timedelta(365)


    #light cycle (12 hour schedule) using apscheduler let's specific sections of the code run at set time intervals, useful for different cycles

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def scheduled_job():
    return

sched.configure(options_from_ini_file)
sched.start()


io.setmode(ioBCM)
io.setup(4,io.OUT)
while True:
    io.output(4,0)
    time.sleep(0,30)
    io.output(4,1)
    time.sleep(0,30)


