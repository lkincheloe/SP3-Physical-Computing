from gpiozero import LED, Button, SPIDevice
import time
import math
import os
from ADCDevice import *

adc = ADCDevice()
led = LED(17)
button = Button(18)

led0 = LED(24)
led1 = LED(21)
led2 = LED(20)
led3 = LED(16)
led4 = LED(12)
led5 = LED(19)
led6 = LED(13)
led7 = LED(5)
led8 = LED(25)

def pressed():
    led.on()
    if value < 25.3:
        led0.on()
    if value < (25.3*2):
        led1.on()
    if value < (25.3*3):
        led2.on()
    if value < (25.3*4):
        led3.on()
    if value < (25.3*5):
        led4.on()
    if value < (25.3*6):
        led5.on()
    if value < (25.3*7):
        led6.on()
    if value < (25.3*8):
        led7.on()
    if value < (25.3*9):
        led8.on()
    time.sleep(0.1)
    if button.is_pressed:
        time.sleep
        pressed()

def released():
    led.off()
    led0.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    
def loop():
    while True:
        time.sleep(0.1)
        button.when_pressed = pressed
        time.sleep(0.1)
        button.when_released = released
        print("testing")
        
        global value
        value = adc.analogRead(0)    # read the ADC value of channel 0
        voltage = value / 255.0 * 3.3  # calculate the voltage value
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.1)

def destroy():
    adc.close()

def start():
    if __name__ == '__main__':
        print ('Program is starting...')
        global adc
        if(adc.detectI2C(0x4b)):
            adc = ADS7830()
        else:
            print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n");
        try:
            loop()
        except KeyboardInterrupt:
            destroy()

start()