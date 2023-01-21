
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('program started')
while True:

    input_state = GPIO.input(20)
    if input_state == False:
            print('Button 1 Pressed')
            time.sleep(0.2)
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button 2 pressed')
        time.sleep(0.2)
        
    
