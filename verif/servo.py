from gpiozero import AngularServo
from time import sleep

# servo = AngularServo(24, min_angle=0, max_angle=180)
# servo.angle = 180
# sleep(0.3)
# del servo

for i in range(0,181,45):
    servo = AngularServo(23, min_angle=0, max_angle=180)
    servo.angle = i
    print(i)
    sleep(0.5)
    del servo
    sleep(2)