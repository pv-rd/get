import RPi.GPIO as gp
import time 
from dec2bin import *
from adc_plot import *
from r2r_adc import *
from mcp3021_driver import *


if __name__ == "__main__":
    try:
        dynamic_range = 5.165
        adc = MCP3021(dynamic_range)
        v = []
        t = []
        dv = []
        dur = 3.0

        start = time.time()
        nw = start
        while time.time() - start <= dur:
            try:
                nw = time.time()
                v.append(adc.get_voltage())
                dv.append(time.time() - nw)
                t.append(time.time() - start) 

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
        
        plot_voltage_vs_time(t, v)
        plot_sampling_period_hist(dv, xlim = 0.1)

    finally:
        adc.deinit()
        


    