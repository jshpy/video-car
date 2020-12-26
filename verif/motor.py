from gpiozero import LED, PWMLED
import time


IN4 = LED(6)
IN3 = LED(13) 
IN2 = LED(19)
IN1 = LED(26)

ENA = PWMLED(20)
ENB = PWMLED(21)

def main():
    while True:
        # 左轮 ENA
        ENA.value = 0.2
        IN1.off()
        IN2.on()
        time.sleep(1) # ⬆后退
        ENA.value = 1
        IN1.on()
        IN2.off()
        time.sleep(1) # ⬆前进

        # # 右轮 ENB 
        # IN3.off()
        # IN4.on()
        # time.sleep(1) # ⬆后退
        # IN3.on()
        # IN4.off()
        # time.sleep(1) # ⬆前进

if __name__ == "__main__":   
    try:
        main()
    except Exception as e:
        print(e)  