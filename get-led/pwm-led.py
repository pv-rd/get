import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
led = 26
buttom = 13
ind = 6
gp.setup(led, gp.OUT)
gp.setup(ind, gp.IN)
st = 1
pwm = gp.PWM(led, 200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty += 1.0
    if duty > 100.0:
        duty = 0.0