from ev3dev import ev3

sensor = ev3.ColorSensor()
sensor.mode = sensor.MODE_RGB_RAW

while True:
    print(sensor.color)