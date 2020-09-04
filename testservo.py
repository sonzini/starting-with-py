#!/usr/bin/env python

# testservo.py

import time

import pigpio

pi = pigpio.pi()  # Connect to local Pi.

# set gpio modes
pi.set_mode(2, pigpio.OUTPUT)


# start 1500 us servo pulses on gpio2
pi.set_servo_pulsewidth(2, 1500)
time.sleep(1)
# for _i in range(5):  # loop between -90 and 90 degrees
#   pi.set_servo_pulsewidth(2, 2500)
#   time.sleep(1)
#   pi.set_servo_pulsewidth(2, 600)
#   time.sleep(1)
#   pi.set_servo_pulsewidth(2, 1500)
#   time.sleep(1)

# pi.set_servo_pulsewidth(2, 0)  # stop servo pulses

# pi.stop()  # terminate connection and release resources

while 1:
  pi.set_servo_pulsewidth(2, 2500)
  time.sleep(1)
  pi.set_servo_pulsewidth(2, 600)
  time.sleep(1)
  pi.set_servo_pulsewidth(2, 1500)
  time.sleep(1)