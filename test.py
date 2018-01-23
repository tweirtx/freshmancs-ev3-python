#!/usr/bin/env python3

from ev3dev import ev3
print("Hello world!")
ev3.Sound.speak("Hello world!")
m = ev3.LargeMotor('outA')
m.run_forever(speed_sp=1000)