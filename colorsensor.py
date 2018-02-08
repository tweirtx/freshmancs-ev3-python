from ev3dev import ev3

leftMotor = ev3.LargeMotor('outA')
rightMotor = ev3.LargeMotor('outB')

sensor = ev3.ColorSensor()

while sensor.color != 1:
    leftMotor.run_forever(speed_sp=900)
    rightMotor.run_forever(speed_sp=900)
leftMotor.stop()
rightMotor.stop()