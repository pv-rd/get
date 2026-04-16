import signal_generator as sg
import time 
import mcp4725_driver as mcp

A = 1.5
f = 5
F = 500

dynamic_range = 3.3
t = 0

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725( dynamic_range, verbose=False)

        while True:
            try:
                dac.set_voltage(A * sg.get_sin_wave_amplitude(f, t))
                sg.wait_for_sampling_period(F)
                t += 1/F
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()