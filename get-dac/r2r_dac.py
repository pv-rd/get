import RPi.GPIO as gp
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

    @staticmethod
    def voltage_to_number(voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f}) В")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / dynamic_range * 255)
    
    def set_voltage(self, voltage):
        self.set_number(self.voltage_to_number(voltage))



leds = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3

if __name__ == "__main__":
    try:
        dac = R2R_DAC(leds, dynamic_range, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()