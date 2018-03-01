from ev3dev import ev3
from math import pi

leftMotor = ev3.LargeMotor('outC')
leftMotor.stop_action = leftMotor.STOP_ACTION_BRAKE
rightMotor = ev3.LargeMotor('outB')
rightMotor.stop_action = rightMotor.STOP_ACTION_BRAKE
ts = ev3.TouchSensor()
print("Setup complete")

def touchsensormeasure():
    print("Function called")
    startingValue = leftMotor.position / leftMotor.count_per_rot
    print("Starting value obtained")
    leftMotor.run_forever(speed_sp=500)
    rightMotor.run_forever(speed_sp=500)
    print("Motors running")
    print(startingValue)
    while not ts.is_pressed:
        print("While loop")
        rotations = leftMotor.position / leftMotor.count_per_rot
        print(rotations)
    print("While loop exited")
    leftMotor.stop()
    rightMotor.stop()
    print("Motors stopped")
    rotation_distance = rotations - startingValue
    radius = 3.5
    distance = rotation_distance * 2 * pi * radius
    distance = distance / 100
    print(distance)

try:
    print("Trying")
    touchsensormeasure()
except BaseException as e:
    print("Excepted")
    print(e)
    leftMotor.stop()
    rightMotor.stop()