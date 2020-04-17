import RPi.GPIO as GPIO
from time import sleep

bump_sensor1 = 17
bump_sensor2 = 4
bump_sensor3 = 27
bump_sensor4 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(bump_sensor1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor4, GPIO.IN, GPIO.PUD_DOWN)

def bump():
    if (GPIO.input(bump_sensor1) or GPIO.input(bump_sensor2) or GPIO.input(bump_sensor3) or GPIO.input(bump_sensor4)):
        return True
    else:
        return False
