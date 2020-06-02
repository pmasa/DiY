import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor

GPIO.setmode(GPIO.BCM)

relay_pin = 27
pir_sensor = 17

GPIO.setup(relay_pin, GPIO.OUT)
pir = MotionSensor(pir_sensor)

print ("Pause de 2 secondes")
time.sleep(2)


print ("Debut du processus...")


try:
    while True:
        time.sleep(0.5)    
        if pir.motion_detected:
            
            print("Demarrage pompe")
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(0.005)

            print("Arret pompe")
            GPIO.output(relay_pin, GPIO.LOW)
            time.sleep(10)

except KeyboardInterrupt:
    print("CTRL-C: stoppe le programme.")
finally:
    print("Nettoyage des GPIO...")
    GPIO.output(relay_pin, GPIO.LOW)
    GPIO.cleanup()


