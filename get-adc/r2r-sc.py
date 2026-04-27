import RPi.GPIO as gp
import time 
from dec2bin import *
from adc_plot import *


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


    def seq(self):
        for val in range(256):
            self.number_to_dac(val)
            time.sleep(self.comp_time)
            if gp.input(self.comp):
                return val
        return val
    
    def get_sc_voltage(self):
        val = self.seq()
        return val/255*self.dyn_range


if __name__ == "__main__":
    try:
        dynamic_range = 3.3
        adc = R2R_ADC(dynamic_range, 0.0001)
        v = []
        t = []
        dv = []
        dur = 3.0

        start = time.time()
        nw = start
        while time.time() - start <= dur:
            try:
                nw = time.time()
                v.append(adc.get_sc_voltage())
                dv.append(time.time() - nw)
                t.append(time.time() - start) 

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
        
        plot_voltage_vs_time(t, v)
        plot_sampling_period_hist(dv)

    finally:
        adc.deinit()
        


    