import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
led=15
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)

while True:
    GPIO.output(led,True)
    print("LED ON")
    sleep(3)
    GPIO.output(led,False)
    print("LED OFF")
    sleep(3)
GPIO.cleanup()
    
