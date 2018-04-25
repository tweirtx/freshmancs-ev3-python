print("Initializing")
from ev3dev import ev3

sensor = ev3.UltrasonicSensor()
stopbutton = ev3.TouchSensor()
left = ev3.LargeMotor('outA')
right = ev3.LargeMotor('outB')
sensor.mode = sensor.MODE_US_DIST_IN

print("Initialized! Press enter to start fighting")
input("Press enter")

while True:
    distance = sensor.distance_inches
    if distance < 6:
        print("Robot detected, ATTACKING!")
        right.run_forever(speed_sp=1000)
        left.run_forever(speed_sp=1000)
    else:
        print("No robot detected, spinning")
        right.run_forever(speed_sp=1000)
        left.run_forever(speed_sp=-1000)
    if stopbutton.is_pressed:
        print("Stop button pressed")
        break
