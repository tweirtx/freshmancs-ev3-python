print("Initializing")
from ev3dev import ev3

sensor = ev3.UltrasonicSensor()
stopbutton = ev3.TouchSensor()
left = ev3.LargeMotor('outC')
right = ev3.LargeMotor('outB')
flippyboi = ev3.MediumMotor('outA')
sensor.mode = sensor.MODE_US_DIST_IN
lights = ev3.Leds()

print("Initialized! Press enter to start fighting")
input("Press enter")

while True:
    distance = sensor.distance_inches
    if distance < 6:
        print("Robot detected, ATTACKING!")
        lights.red_left
        lights.red_right
        right.run_forever(speed_sp=-900)
        left.run_forever(speed_sp=-900)
        flippyboi.run_to_rel_pos(speed_sp=1000, position_sp=-1)
        flippyboi.run_to_rel_pos(speed_sp=1000, position_sp=1)
    else:
        print("No robot detected, spinning")
        lights.set_color(lights.LEFT, lights.ORANGE)
        lights.set_color(lights.RIGHT, lights.ORANGE)
        right.run_forever(speed_sp=900)
        left.run_forever(speed_sp=-900)
    if stopbutton.is_pressed:
        print("Stop button pressed")
        lights.green_left
        lights.green_right
        left.stop()
        right.stop()
        flippyboi.stop()
        break
