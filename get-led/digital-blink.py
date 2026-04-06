import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
led = 26
gp.setup(led, gp.OUT)
st = 0
per = 3
while True:
    gp.output(led, st)
    st = not st
    time.sleep(per)