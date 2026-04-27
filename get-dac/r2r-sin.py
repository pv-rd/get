import r2r_dac as r2r
import signal_generator as sg
import time 
import PWM_DAC as pwm

A = 1.5
f = 5
F = 1000

leds = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
t = 0

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC(leds, dynamic_range, True)
        duty = 0.0
        v = 1
        while True:
            try:
                while True:
                    time.sleep(0.001)
                    duty += v
                    if duty >= 100.0 or duty <= 0.0:
                        v  = -v

                    dac.set_voltage(duty * dynamic_range / 100)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()