#!/usr/bin/env python3
import time

from ev3dev import ev3
leftmotor = ev3.LargeMotor('outA')
rightmotor = ev3.LargeMotor('outB')

leftmotor.run_forever(speed_sp=500)
rightmotor.run_forever(speed_sp=1000)
time.sleep(5)
leftmotor.stop()
rightmotor.stop()
