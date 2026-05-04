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

    def number_to_dac(self, number):
        gp.output(self.bits, [int(el) for el in bin(number)[2:].zfill(8)])



    #def number_to_dac(self, number):
    #    leds = [26, 20, 19, 16, 13, 12, 25, 11]
    #    R2R_DAC(leds, self.dyn_range, True).set_voltage(number/255*self.dyn_range)

    def seq(self):
        for val in range(256):
            self.number_to_dac(val)
            time.sleep(0.01)
            if gp.input(self.comp):
                return val
        return 255
    
    def get_sc_voltage(self):
        val = self.seq()
        return val/255*self.dyn_range

    def sar_adc(self):
        N = 8
        A = [0]*8
        for i in range(N):
            A[i] = 1
            gp.output(self.bits, A)
            time.sleep(self.comp_time)
            if gp.input(self.comp):
                A[i] = 0
            
        val = 0
        for i in range(N):
            if A[i] == 1: val += 2**(7-i)
        return val

    
    def get_sar_voltage(self):
        val = self.sar_adc()
        return val/255*self.dyn_range*1.65/1.64
        


if __name__ == "__main__":
    try:
        dynamic_range = 3.22
        adc = R2R_ADC(dynamic_range)

        while True:
            try:
                voltage1 = adc.get_sc_voltage()
                voltage2 = adc.get_sar_voltage()
                print("SC:", voltage1, "SAR:", voltage2)
                

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        adc.deinit()
        


    