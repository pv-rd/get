import RPi.GPIO as gp
import smbus
import time
from dec2bin import *

class MCP3021:
    def __init__(self, dynamic_range, address =0x4D, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        l = data >> 8
        u = data & 0xFF
        num = (u << 6) | (l >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, старший байт: {u:x}, младший байт {l:x}, число {num}")
        return num

    def get_voltage(self):
        val = self.get_number()
        return val/1024*self.dynamic_range

    def deinit(self):
        self.bus.close()


if __name__ == "__main__":
    try:
        dynamic_range = 5.165
        adc = MCP3021(dynamic_range)

        while True:
            try:
                voltage1 = adc.get_voltage()
                print("MCP3021:", voltage1)
                time.sleep(1)
                

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        adc.deinit()