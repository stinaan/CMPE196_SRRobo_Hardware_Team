import RPi.GPIO as GPIO
from time import sleep

bump_sensor1 = 17
bump_sensor2 = 4
bump_sensor3 = 27
bump_sensor4 = 22

# motor setup
en1 = 12
en2 = 16
in1 = 5
in2 = 6
in3 = 13
in4 = 19


GPIO.setmode(GPIO.BCM)
GPIO.setup(bump_sensor1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor4, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

def forward():
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)
    print('Forward')

def stop():
    GPIO.output(in1, 0)
    GPIO.output(in2, 0)
    GPIO.output(in3, 0)
    GPIO.output(in4, 0)
    print('Stop')

while (1):
    go_forward = True
    if GPIO.input(bump_sensor1):
        stop()
        go_forward = False
        print('BUMP SENSOR 1 IS ACTIVE')
    if GPIO.input(bump_sensor2):
        stop()
        go_forward = False
        print('BUMP SENSOR 2 IS ACTIVE')
    if GPIO.input(bump_sensor3):
        stop()
        go_forward = False
        print('BUMP SENSOR 3 IS ACTIVE')
    if GPIO.input(bump_sensor4):
        stop()
        go_forward = False
        print('BUMP SENSOR 4 IS ACTIVE')
    if (go_forward):
        forward()
    sleep(1)
