import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
led = 26
buttom = 13
ind = 6
gp.setup(led, gp.OUT)
gp.setup(ind, gp.IN)
st = 1
while True:
    gp.output(led, gp.input(ind))
    time.sleep(0.2)