from ev3dev import ev3
from time import sleep

gyro = ev3.GyroSensor('in4')
gyro.mode = gyro.MODE_GYRO_ANG
leftMotor = ev3.LargeMotor('outA')
rightMotor = ev3.LargeMotor('outB')
print("Defined")

while gyro.angle != 360:
    print(gyro.angle)
    leftMotor.run_forever(speed_sp=900)
    rightMotor.run_forever(speed_sp=-900)
print("Gyro angle is target")
leftMotor.stop_action = leftMotor.STOP_ACTION_BRAKE
rightMotor.stop_action = rightMotor.STOP_ACTION_BRAKE

leftMotor.stop()
rightMotor.stop()