import r2r_dac as r2r
import signal_generator as sg
import time 
import PWM_DAC as pwm



if __name__ == "__main__":
    A = 3
    f = 10
    F = 1000

    pin = 12
    dynamic_range = 3.3
    t = 0
    try:
        dac = pwm.PWM_DAC(pin, F, dynamic_range, True)

        while True:
            try:
                dac.set_voltage(A* sg.get_sin_wave_amplitude(f, t))
                sg.wait_for_sampling_period(F)
                t += 1/F
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()