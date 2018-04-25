print("Initializing...")
from ev3dev import ev3
from time import sleep

motor1 = ev3.LargeMotor('outA')
motor2 = ev3.LargeMotor('outC')
motor3 = ev3.LargeMotor('outD')

print("Initialization complete!")

input("Press enter to start")

ramp_up_speed = 300

motor1.run_forever(speed_sp=ramp_up_speed)
motor2.run_forever(speed_sp=ramp_up_speed)
motor3.run_forever(speed_sp=ramp_up_speed)
print("sleeping")
sleep(0.1)
print("waking up")
motor1.run_forever(speed_sp=1000)
motor2.run_forever(speed_sp=1000)
motor3.run_forever(speed_sp=1000)

input("Press enter to stop")

motor1.stop_action = motor1.STOP_ACTION_BRAKE
motor1.stop()

motor2.stop_action = motor2.STOP_ACTION_BRAKE
motor2.stop()

motor3.stop_action = motor3.STOP_ACTION_BRAKE
motor3.stop()
