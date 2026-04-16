import RPi.GPIO as gp

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin

        gp.setmode(gp.BCM)
        gp.setup(self.gpio_pin, gp.OUT)

        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency = pwm_frequency

        self.pwm = gp.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(100)


    def deinit(self):
        gp.output(self.gpio_pin, 0)
        gp.cleanup()

    
    def set_voltage(self, voltage):

        duty = voltage/self.dynamic_range
        self.pwm.ChangeDutyCycle(duty*100)
        
        

"""dynamic_range = 3.3
pin = 12
f = 200

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, dynamic_range, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()"""