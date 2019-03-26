import datetime
from apscheduler import BlockingScheduler
import GPIO as io
import RPi.GPIO as GPIO
import signal
import subprocess
import os
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

rec_proc = None
try:
    while True:
        if GPIO.input(4):
            GPIO.output(25, 1)
            if rec_proc is None:
                rec_proc = subprocess.Popen("/script/start.sh",
                           shell=True, preexec_fn=os.setsid)
        else:
            GPIO.output(25, 0)
            if rec_proc is not None:
                os.killpg(rec_proc.pid, signal.SIGTERM)
                rec_proc = None
        sleep(0.2)

finally:
    GPIO.cleanup()


time.sleep(.1)

class(components):
    def __init__(self, watercycle, lightcycle, pump, io, apscheduler, datetime):
        self.watercycle = watercycle
        self.pump = pump
        self.lightcycle = lightcycle
        self.io = io
        assert isinstance(apscheduler, BlockingScheduler)
        self.apscheduler = apscheduler
        self.z = datetime


pump_start = io

# water cycle
while True:

    time.localtime(time.time())

    # pump time (seconds) Adjust according to pump intensity and diameter of tubing
    if True:
        pump.pump = time.time() + 5
    then

    1 < time.clock()

    pump_Start
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
