import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
while(True):
    GPIO.output(22, GPIO.HIGH)
    print('program says beeeeeeeeeppp!')
    sleep(0.5)
    GPIO.output(22, GPIO.LOW)
    print('program says no beep :(')
    sleep(0.5)
exit();
    
