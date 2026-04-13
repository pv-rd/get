import RPi.GPIO as gp
import smbus

class MCP4725:
    def __init__(self, dynamic_range, address =0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range


    def deinit(self):
        self.bus.close()

    
    def set_number(self, number):
        if not isinstance(number, int):
            print("Только Z")
        
        elif not (0 <= number <= 4095):
            print("Выход за разрядность 12 бит")
        
        else:
            first_byte = self.wm | self.pds | number >> 8
            second_byte = number & 0xFF
            self.bus.write_byte_data(0x61, first_byte, second_byte)

            if self.verbose:
                print(f"Число: {number}, отправленые по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")


        
        

dynamic_range = 3.3
pin = 12
f = 200

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, dynamic_range, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()