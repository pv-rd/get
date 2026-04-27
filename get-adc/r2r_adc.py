import RPi.GPIO as gp
import time 
from dec2bin import *

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gp.setmode(gp.BCM)
        gp.setup(self.gpio_bits, gp.OUT, initial = 0)

    def deinit(self):
        gp.output(self.gpio_bits, 0)
        gp.cleanup()

    def set_number(self, number):
        gp.output(self.gpio_bits, dec2bin(number))

    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f}) В")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / self.dynamic_range * 255)
    
    def set_voltage(self, voltage):
        self.set_number(self.voltage_to_number(voltage))


class R2R_ADC:
    def __init__(self, dyn_range, comp_time = 0.01, verbose = False):
        self.dyn_range = dyn_range
        self.comp_time = comp_time
        self.verbose = verbose

        self.bits = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp = 21

        gp.setmode(gp.BCM)
        gp.setup(self.bits, gp.OUT, initial = 0)
        gp.setup(self.comp, gp.IN)


    def deinit(self):
        gp.output(self.bits, 0)
        gp.cleanup()

    #def number_to_dac(self, number):
    #    gp.output(self.bits, [int(el) for el in bin(number)[2:].zfill(8)])

    def number_to_dac(self, number):
        leds = [26, 20, 19, 16, 13, 12, 25, 11]
        R2R_DAC(leds, self.dyn_range, True).set_voltage(number/255*self.dyn_range)

    def seq(self):
        for val in range(256):
            self.number_to_dac(val)
            time.sleep(0.01)
            print(gp.input(self.comp))
            if gp.input(self.comp):
                return val
        return val
    
    def get_sc_voltage(self):
        val = self.seq()
        return val/255*self.dyn_range


if __name__ == "__main__":
    try:
        dynamic_range = 3.3
        adc = R2R_ADC(dynamic_range )

        while True:
            try:
                voltage = adc.get_sc_voltage()
                print(voltage)
                

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        adc.deinit()
        


    