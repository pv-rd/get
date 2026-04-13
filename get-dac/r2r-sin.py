import r2r_dac as r2r
import signal_generator as sg
import time 
import PWM_DAC as p

A = 3.2
f = 10
F = 1000

leds = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
t = 0

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC(leds, dynamic_range, True)
        dac2 = p.PWM_DAC(12, 200, dynamic_range, True)

        while True:
            try:
                dac.set_voltage(dynamic_range * sg.get_sin_wave_amplitude(f, t))
                dac2.set_voltage(dynamic_range * sg.get_sin_wave_amplitude(f*2, t))
                sg.wait_for_sampling_period(F)
                t += 1/F
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()
        dac2.deinit()