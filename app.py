from gpiozero import LED, PWMLED
from controller import SingleSerov

import time

from controller import CarDriver

carConfig = {
        "CA1": 22,
        "CA2": 27,
        "SA": 20,
        "CB1": 17,
        "CB2": 4,
        "SB": 21,
    }
car = CarDriver(**carConfig)
car.speed = 1

guang = PWMLED(18)

ser_v = SingleSerov(24) # 垂直
ser_h = SingleSerov(23, 90) # 水平



def main():
    while True:
        v = input(':')
        car.speed = 1
        if v=='w':
            car.up()
        elif v=='s':
            car.down()
        elif v=='a':
            car.left()
        elif v=='d':
            car.right()
        elif v=='q':
            guang.pulse()
        elif v=='e':
            guang.value = 0
        elif v=='r':
            ser_v.toStart()
        elif v=='f':
            ser_v.toEnd()
        elif v=='z':
            ser_h.toEnd()
        elif v=='x':
            ser_h.toStart()
        elif v==' ':
            car.stop()
            
        # time.sleep(1)

if __name__ == "__main__":
    main()