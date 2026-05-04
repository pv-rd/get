import RPi.GPIO as gp
import time 
from dec2bin import *
from adc_plot import *
from r2r_adc import *


if __name__ == "__main__":
    try:
        dynamic_range = 3.367
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
                v.append(adc.get_sar_voltage())
                dv.append(time.time() - nw)
                t.append(time.time() - start) 

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
        
        plot_voltage_vs_time(t, v)
        plot_sampling_period_hist(dv)

    finally:
        adc.deinit()
        


    