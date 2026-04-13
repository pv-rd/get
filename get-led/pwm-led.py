import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
led = 12
gp.setup(led, gp.OUT)
pwm = gp.PWM(led, 200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty += 1.0
    if duty > 100.0:
        duty = 0.0