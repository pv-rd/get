import signal_generator as sg
import time 
import mcp4725_driver as mcp

A = 1.5
f = 5
F = 500

dynamic_range = 5
t = 0

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725( dynamic_range, verbose=False)
        duty = 0.0
        v = 1
        while True:
            try:
                while True:
                    time.sleep(0.001)
                    duty += v
                    if duty >= 100.0 or duty <= 0.0:
                        v  = -v

                    dac.set_voltage(duty * dynamic_range / 150)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()