import RPi.GPIO as gp
import time 

class R2R_ADC:
    def __init__(self, dyn_range, comp_time = 0.01, verbose = False):
        self.dyn_range = dyn_range
        self.comp_time = comp_time
        self.verbose = verbose

        self.bits = [26, 20, 19, 16, 13, 12, 25, 11]

        gp.setmode(gp.BCM)
        gp.setup(self.bits, gp.OUT, initial = 0)
        


    def deinit(self):
        gp.output(self.bits, 0)
        gp.cleanup()

    def number_to_dac(self, number):
        gp.output(self.bits, [int(el) for el in bin(number)[2:].zfill(8)])




if __name__ == "__main__":


    gp.setmode(gp.BCM)

    gp.setup(21, gp.IN)

    try:
        adc = R2R_ADC(3.3)

        while True:
            try:

                for val in range(256):
                    adc.number_to_dac(val)
                    time.sleep(0.1)
                    print(gp.input(21))
                

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        adc.deinit()
        