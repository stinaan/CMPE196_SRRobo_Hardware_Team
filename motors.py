import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

en1 = 12
en2 = 16
in1 = 5
in2 = 6
in3 = 13
in4 = 19

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

def reverse():
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)

def right_turn():
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)

def left_turn():
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)

def stop():
    GPIO.output(in1, 0)
    GPIO.output(in2, 0)
    GPIO.output(in3, 0)
    GPIO.output(in4, 0)

