from gpiozero import LED, PWMLED
import time


# laser = LED(18)

laserPwm = PWMLED(18)

def main():
    # laser.on()
    while True:
        for i in range(1,11):
            laserPwm.value = i/10
            print(i/10)
            time.sleep(1)

if __name__ == "__main__":   
    try:
        main()
    except Exception as e:
        print(e)  