
import RPi.GPIO as GPIO # import de la librairie de gestion des GPIO
import time  # import de la librairie de gestion du temps

from gpiozero import MotionSensor # import de la librairie de gestion du capteur

GPIO.setmode(GPIO.BCM) # les pins sont lus selon leur numérotation électronique
pin_relais = 27
pin_capteur = 17

GPIO.setup(pin_relais, GPIO.OUT) # Initialisation du pin relais en sortie

capteur = MotionSensor(pin_capteur) # Initialisation de l'objet capteur

print ("Pause de 2 secondes")
time.sleep(2)
print ("Debut du processus...")

try:
    # début boucle infinie
    while True:
            
        if capteur.motion_detected: # capteur détecte mouvement ?
            # le capteur a detecté un mouvement
            print("Demarrage pompe")
            GPIO.output(pin_relais, GPIO.HIGH)
            time.sleep(0.005) # temps nécessaire pour aspirer le liquide

            print("Arret pompe")
            GPIO.output(pin_relais, GPIO.LOW)
            time.sleep(10) # temporisation de 10 sec pour réinitialiser le capteur

        time.sleep(0.5) # temporisation de 0.5sec pour ne pas chauffer le processeur

except KeyboardInterrupt:
    print("CTRL-C: stoppe le programme.")
finally:
    print("Nettoyage des GPIO...")
    GPIO.cleanup()
