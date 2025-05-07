from __future__ import division
import time

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

ANGLE_INIT = 425
ANGLE_90 = 360
ANGLE_180 = 490

angle = ANGLE_INIT

# Set frequency to 60hz, good for servos
pwm.set_pwm_freq(60)


def setup(dir_ch):
    pwm.set_pwm(dir_ch, 0, ANGLE_INIT)  # dir_mid to be changed


def turn_left(dir_ch):
    global angle
    if angle >= 615:
        print("teering gear reached its peak")
    else:
        angle += 10
        pwm.set_pwm(dir_ch, 0, angle)


def turn_right(dir_ch):
    global angle
    if angle <= 260:
        print("teering gear reached its peak")
    else:
        angle -= 10
        pwm.set_pwm(dir_ch, 0, angle)
