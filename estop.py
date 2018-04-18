from ev3dev import ev3

for i in ev3.list_motors():
    i.stop()