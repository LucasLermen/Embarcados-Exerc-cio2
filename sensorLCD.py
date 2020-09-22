import smbus2
import bme280
import RPi_I2C_driver
import time

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_paramentros = bme280.load_calibration_params(bus, endereco)

dado = bme280.sample(bus, endereco, calibracao_paramentros)

print("ID: " + str(dado.id))
print("Data/Hora: " + str(dado.timestamp))
print("Temperatura: " + str(round(dado.temperature, 2)))
print("Umidade: " + str(round(dado.humidity, 2)))
print("Pressão atmosférica: " + str(round(dado.pressure, 2)))

lcdi2c = RPi_I2C_driver.lcd()

lcdi2c.lcd_clear()

while True:
    lcdi2c.lcd_display_string("Temperatura", 1)
    lcdi2c.lcd_display_string(str(round(dado.temperature, 2)), 2)
    time.sleep(1)
    lcdi2c.lcd_clear()

    lcdi2c.lcd_display_string("Umidade", 1)
    lcdi2c.lcd_display_string(str(round(dado.humidity, 2)), 2)
    time.sleep(1)
    lcdi2c.lcd_clear()

    lcdi2c.lcd_display_string("Pressao", 1)
    lcdi2c.lcd_display_string(str(round(dado.pressure, 2)), 2)
    time.sleep(1)
    lcdi2c.lcd_clear()

