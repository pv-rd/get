import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
led = 26
buttom = 13
gp.setup(led, gp.OUT)
gp.setup(buttom, gp.IN)
st = 0
per = 3
while True:
    if gp.input(buttom):
        st = not st
        gp.output(led, st)
        time.sleep(0.2)