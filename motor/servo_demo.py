from __future__ import division
import time

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

dir_mid = 425

add = dir_mid

pwm.set_pwm_freq(60)

CH_MAIN_SERVO = 0  # main axis of turning arm

pwm.set_pwm(CH_MAIN_SERVO, 0, dir_mid)  # dir_mid to be changed


def turn_left(dir_ch):
    global add
    if add >= 615:
        print("teering gear reached its peak")
    else:
        add += 10
        pwm.set_pwm(dir_ch, 0, add)


for i in range(10):
    turn_left(CH_MAIN_SERVO)
