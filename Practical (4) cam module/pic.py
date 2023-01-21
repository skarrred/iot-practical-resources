import time as tm
from picamera import PiCamera
cam = PiCamera()
cam.resolution = (1280, 720)
tm.sleep(3)
cam.capture('/home/pi/Desktop/Ammar.jpg')
cam.stop_preview()
print('photo le liya')
