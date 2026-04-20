import RPi.GPIO as gp
import time
class Triangle():

    def __init__(self, led = 12, F = 200, v = 1, f = 0.05):
        
        gp.setmode(gp.BCM)
        self.led = led
        self.step_value = v
        self.step_time = 1/f
        self.f = F
        gp.setup(led, gp.OUT)
        pwm = gp.PWM(self.led, self.f)
        duty = 0.0
        pwm.start(duty)
        while True:
            pwm.ChangeDutyCycle(duty)
            time.sleep(self.step_time)
            duty += self.step_value
            if duty >= 100.0 or duty <= 0.0:
                self.step_value  = -self.step_value

if __name__ == "__main__":
    try:
        dac = Triangle(F = 1000, f = 100)
    finally:
        dac.deinit()