from component.Motor import SingleMotor


class CarDriver(object):
    '''
    motorA --> Left
    motorB --> Right
    '''
    def __init__(self, **motorConfig):
        self.motorA = SingleMotor(motorConfig.get("CA1"), motorConfig.get("CA2"), motorConfig.get("SA")) 
        self.motorB = SingleMotor(motorConfig.get("CB1"), motorConfig.get("CB2"), motorConfig.get("SB")) 
        self._speed = 0.8

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float):
        self._speed = speed

    def up(self, offset=(1,1)):
        self.__adjustSpeed(offset)
        self.motorA.forward()
        self.motorB.forward()

    def down(self, offset=(1,1)):
        self.__adjustSpeed(offset)
        self.motorA.reverse()
        self.motorB.reverse()

    def left(self, offset=(1,1)):
        self.__adjustSpeed(offset)
        self.motorA.reverse()
        self.motorB.forward()

    def right(self, offset=(1,1)):
        self.__adjustSpeed(offset)
        self.motorA.forward()
        self.motorB.reverse()

    def stop(self):
        self.speed = 0
        self.up()


    def __adjustSpeed(self, offset):
        ofsA, ofsB = offset
        self.motorA.speed = ofsA * self.speed
        self.motorB.speed = ofsB * self.speed


if __name__ == "__main__":
    import time

    carConfig = {
        "CA1": 26,
        "CA2": 19,
        "SA": 20,
        "CB1": 13,
        "CB2": 6,
        "SB": 21,
    }
    car = CarDriver(**carConfig)

    for i in range(1,11):
        car.speed = i/10
        car.up()

        print(i/10)
        time.sleep(1)