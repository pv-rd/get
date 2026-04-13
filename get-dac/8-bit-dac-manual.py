import RPi.GPIO as gp

gp.setmode(gp.BCM)
#leds = [16, 12, 25, 17, 27, 23, 22, 24]
leds = [16, 20, 21, 25, 26, 17, 27, 22]
gp.setup(leds, gp.OUT)
gp.output(leds, 0)



dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f}) В")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    dec2bin = [int(el) for el in bin(number)[2:].zfill(8)]
    gp.output(leds, dec2bin)


s_time = 0.2

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    gp.output(leds, 0)
    gp.cleanup()