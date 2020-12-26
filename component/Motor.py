from gpiozero import LED, PWMLED

from abc import ABC, abstractmethod

class Motor(ABC):

    """
    单个电机类
    """
    @abstractmethod
    def forward(self):
        '''
        正转
        '''
        pass

    @abstractmethod
    def reverse(self):
        '''
        反转
        '''
        pass


class SingleMotor(Motor):
    """
    单个电机的控制类
    """
    def __init__(self, C1: int, C2: int, S:float):
        """
        C1 控制端1
        C2 控制端2
        S 调速端
        """
        self._IN1 = LED(C1)
        self._IN2 = LED(C2)
        self._EN = PWMLED(S)
        self._speed = 0

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float):
        self._EN.value = speed
        self._speed = speed

    def forward(self):
        '''
        正转
        '''
        self._EN.value = self._speed
        self._IN1.on()
        self._IN2.off()

    def reverse(self):
        '''
        反转
        '''
        self._EN.value = self._speed
        self._IN1.off()
        self._IN2.on()



if __name__ == "__main__":
    import time
    # 左电机
    # s1 = SingleMotor(26, 19, 20)
    # 右电机
    s1 = SingleMotor(13, 6, 21)
    for i in range(10):
        s1.speed = i/10
        s1.forward()

        print(i/10)
        time.sleep(1)

        s1.reverse()
        time.sleep(1)
