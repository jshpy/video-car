import time

def test_Motor():
    from component import SingleMotor
    # 左电机
    s2 = SingleMotor(19, 26, 20)
    s2.speed = 1
    #s2.forward()
    s2.reverse()
    # 右电机
    # s1 = SingleMotor(6, 13, 21)
    # s1.speed = 1
    # s1.forward()
    # s1.reverse()
    time.sleep(1000)

def test_Car():
    from controller import CarDriver
    carConfig = {
        "CA1": 27,
        "CA2": 22,
        "SA": 20,
        "CB1": 4,
        "CB2": 17,
        "SB": 21,
    }
    car = CarDriver(**carConfig)

    for i in range(10,11):
        car.speed = i/10
        # car.up()
        # car.down()
        # car.left()
        car.right()

        print(i/10)
        time.sleep(1)

def test_Serov():
    from controller import SingleSerov
    ser = SingleSerov(24) # 垂直
    ser2 = SingleSerov(23, 90) # 水平
    ser.toStart()
    ser2.toStart()
    time.sleep(1)
    ser.toStart()
    ser2.toStart()
    time.sleep(1)
    ser.toEnd()
    ser2.toEnd()
    time.sleep(1)
    ser.toEnd()
    ser2.toEnd()

if __name__ == "__main__":
    # test_Motor()
    # test_Car()
    test_Serov()