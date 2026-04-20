import RPi.GPIO as gp
import time
import smbus
import r2r_dac as r2r
import PWM_DAC as p
import mcp4725_driver as mcp
from dec2bin import *
class Triangle():

    def __init__(self, pin = 12, dynamic_range = 3.3, mode = 'pwm', 
    address =0x61,  F = 1000, verbose = True):
        '''pwm, r2r, mcp4725'''

        self.mode = mode
        self.pin = pin 
        self.F = F     
        gp.setmode(gp.BCM)
        gp.setup(pin, gp.OUT)
        self.verbose = verbose
        self.dynamic_range = dynamic_range

        self.duty = 0.0 

        if self.mode == 'mcp4725':
            self.bus = smbus.SMBus(1)
            self.address = address
            self.wm = 0x00
            self.pds = 0x00

        elif self.mode == 'pwm':
            self.pwm = gp.PWM(self.pin, self.F)
            self.pwm.start(self.duty)

    def set(self, voltage):
        if self.mode == 'r2r':
            r2r.R2R_DAC(self.pin, self.dynamic_range, True).set_voltage(voltage)
        
        elif self.mode == 'mcp4725':
            mcp.MCP4725(self.dynamic_range, self.address, self.verbose).set_voltage(voltage)

        elif self.mode == 'pwm':
            p.PWM_DAC(self.pin, self.F, self.dynamic_range, self.verbose).set_voltage(voltage)
        

    def start(self, F = 1000, f = 100, v = 1):
        self.F = F
        self.f = f
        self.v = v
        while True:
            time.sleep(1/self.f)
            self.duty += self.v
            if self.duty >= 100.0 or self.duty <= 0.0:
                self.v  = -self.v
    def deinit(self):
        if self.mode == 'mcp4725':
            self.bus.close()
        elif self.mode == 'r2r':
            gp.output(self.pin, 0)
            gp.cleanup()



if __name__ == "__main__":
    try:
        dac1 = Triangle()
        dac2 = Triangle(mode='r2r', pin = [16, 20, 21, 25, 26, 17, 27, 22])
        dac3 = Triangle(mode='mcp4725')

        dac1.start()
        dac2.start()
        dac3.start()


    finally:
        dac1.deinit()
        dac2.deinit()
        dac3.deinit()