import RPi.GPIO as GPIO
import time

K_pin = 17
button_pin = 23
status = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(K_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(K_pin, True)

while True:
    while GPIO.input(button_pin) == status:
        if GPIO.input(button_pin):
            GPIO.output(K_pin, False)
            print('按钮按下，继电器吸合')
            status = False
        else:
            GPIO.output(K_pin, True)
            print('按钮抬起，继电器断开')
            status = True
    time.sleep(0.05)

GPIO.cleanup()
