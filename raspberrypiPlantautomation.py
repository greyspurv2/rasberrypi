import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import Rpi.GPIO as io
import threading


def __init__(self, watercycle, lightcycle, pumpcycle):
    self.watercycle = watercycle
    self.pumpcycle = pumpcycle
    self.lightcycle = lightcycle


# water cycle
while True:

    time.localtime(time.time())

    # pump time (seconds) Adjust according to pump intensity and diameter of tubing
    if True:
        pump.pumpcycle = time.time() + 5
    then


    pumpcycle_start()
    
    if False:
    
    then
    
    pumpcycle.stop()
    
else:
        pump_Stop
        dt = datetime.timedelta(365)

        # light cycle (12 hour schedule) using apscheduler let's specific sections of the code run at set time intervals, useful for different cycles

        sched = BlockingScheduler()


        @sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
        def scheduled_job():
            return


        sched.configure(options_from_ini_file)
        sched.start()

        # pin selction for the pump

        io.setmode(ioBCM)
        io.setup(4, io.OUT)
        while True:
            io.output(4, 0)
            time.sleep(0, 30)
            io.output(4, 1)
            time.sleep(0, 30)

        # pin selction for the lights

        io.setmode(ioBCM)
        io.setup(5, io.OUT)
        while True:
            io.output(5, 0)
            time.sleep(0, 30)
            io.output(5, 1)
            time.sleep(0, 30)
