from ev3dev import ev3

leftMotor = ev3.LargeMotor('outA')
rightMotor = ev3.LargeMotor('outB')

sensor = ev3.ColorSensor()
leftMotor.run_forever(speed_sp=900)
rightMotor.run_forever(speed_sp=900)

while True:
    color = sensor.color
    if color is 0:
        break

leftMotor.stop_action = leftMotor.STOP_ACTION_BRAKE
rightMotor.stop_action = rightMotor.STOP_ACTION_BRAKE
leftMotor.stop()
rightMotor.stop()