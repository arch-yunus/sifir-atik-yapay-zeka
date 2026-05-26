import RPi.GPIO as GPIO
import time

# Servo pimi (örneğin GPIO 18)
SERVO_PIN = 18

def setup_servo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    
    # 50Hz (20ms PWM period) standard servo için
    pwm = GPIO.PWM(SERVO_PIN, 50)
    pwm.start(0)
    return pwm

def set_angle(pwm, angle):
    # Açı değerini (0-180) duty cycle değerine çevir
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def main():
    print("Servo Motor Kontrol Testi Başlatılıyor...")
    try:
        pwm = setup_servo()
        print("0 Derece (PET Haznesi)")
        set_angle(pwm, 0)
        time.sleep(1)
        
        print("90 Derece (HDPE Haznesi)")
        set_angle(pwm, 90)
        time.sleep(1)
        
        print("180 Derece (Metal Haznesi)")
        set_angle(pwm, 180)
        time.sleep(1)
        
    except KeyboardInterrupt:
        print("Test iptal edildi.")
    finally:
        if 'pwm' in locals():
            pwm.stop()
        GPIO.cleanup()
        print("GPIO Temizlendi.")

if __name__ == "__main__":
    main()
