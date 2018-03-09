print("Initializing...")
from ev3dev import ev3

rightMotor = ev3.LargeMotor('outA')
leftMotor = ev3.LargeMotor('outD')
backMotor = ev3.LargeMotor('outB')
rightMotor.stop_action = rightMotor.STOP_ACTION_BRAKE
leftMotor.stop_action = leftMotor.STOP_ACTION_BRAKE
backMotor.stop_action = leftMotor.STOP_ACTION_BRAKE
rightMotor.polarity = rightMotor.POLARITY_INVERSED
speed = 600
print("Initialization complete!")
while True:
    input("Press enter to start the motors ")
    rightMotor.run_forever(speed_sp=speed)
    leftMotor.run_forever(speed_sp=speed)
    backMotor.run_forever(speed_sp=speed)
    input("Press enter to stop the motors ")
    rightMotor.stop()
    leftMotor.stop()
    backMotor.stop()