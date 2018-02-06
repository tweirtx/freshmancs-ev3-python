from ev3dev import ev3
import time

color = ev3.ColorSensor()
color.mode = 'COL-COLOR'
leftMotor = ev3.LargeMotor('outA')
rightMotor = ev3.LargeMotor('outB')

leftMotor.run_to_rel_pos(position_sp=1000, speed_sp=900, stop_action="hold")
rightMotor.run_to_rel_pos(position_sp=1000, speed_sp=900, stop_action="hold")

time.sleep(3)

rightMotor.run_to_rel_pos(position_sp=-190, speed_sp=900, stop_action="hold")
leftMotor.run_to_rel_pos(position_sp=190, speed_sp=900, stop_action="hold")

time.sleep(3)

leftMotor.run_to_rel_pos(position_sp=2000, speed_sp=900, stop_action="hold")
rightMotor.run_to_rel_pos(position_sp=2000, speed_sp=900, stop_action="hold")

time.sleep(10)