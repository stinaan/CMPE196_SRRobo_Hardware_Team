import motors as m
#import bump as b
import RPi.GPIO as GPIO
import time
#new stuff
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import signal

#new stuff
# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/serviceAccountKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://srrobo.firebaseio.com/'
})

def interrupted(signum, frame):
    print ('asdf')
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
        foo = raw_input()
        return foo
    except:
        return

signal.alarm(5)
s = input()
signal.alarm(0)

bump_sensor1 = 17
bump_sensor2 = 4
bump_sensor3 = 27
bump_sensor4 = 22

GPIO.setup(bump_sensor1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(bump_sensor4, GPIO.IN, GPIO.PUD_DOWN)

def my_callback(bump_sensor1):
    m.stop()

GPIO.add_event_detect(bump_sensor1, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(bump_sensor2, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(bump_sensor3, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(bump_sensor4, GPIO.RISING, callback=my_callback)

while (1):
    x = input() 
    # As an admin, the app has access to read and write all data, regradless of Security Rules
    cmd = db.reference('command')

    if x=='w' or cmd == 'Forward':
        m.forward()
    elif x=='a' or cmd == 'Left':
        m.left_turn()
        time.sleep(0.1)
        m.stop()
    elif x=='aa':
        m.left_turn()
        time.sleep(0.4)
        m.stop()
    elif x=='d' or cmd == 'Right':
        m.right_turn()
        time.sleep(0.1)
        m.stop()
    elif x=='dd':
        m.right_turn()
        time.sleep(0.4)
        m.stop()
    elif x=='ss' or cmd == 'Back':
        m.reverse()
    elif x=='s' or cmd == 'End':
        m.stop()
