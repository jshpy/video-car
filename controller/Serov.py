from gpiozero import AngularServo
from time import sleep


class SingleSerov(object):
    """
    docstring
    """
    def __init__(self, ctrlPin:int, angleFragment=45):
        """
        docstring
        """
        self.__angleFragment = angleFragment
        self.__ctrlPin = ctrlPin
        self.__angle = 90
        self.__setup()

    def __setup(self):
        servo = AngularServo(self.__ctrlPin, min_angle=0, max_angle=180)
        servo.angle = self.__angle
        sleep(0.5)
        del servo

    def toStart(self):
        if (self.__angle - self.__angleFragment) >= 0:
            self.__angle -= self.__angleFragment
            servo = AngularServo(self.__ctrlPin, min_angle=0, max_angle=180)
            servo.angle = self.__angle
            sleep(0.5)

    def toEnd(self):
        if (self.__angle + self.__angleFragment) <= 180:
            self.__angle += self.__angleFragment
            servo = AngularServo(self.__ctrlPin, min_angle=0, max_angle=180)
            servo.angle = self.__angle
            sleep(0.5)
