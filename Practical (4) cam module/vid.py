import time as tm
from picamera import PiCamera
cam = PiCamera()
cam.start_preview()
cam.start_recording('/home/pi/Desktop/Ammar.h264')
cam.wait_recording(10)
cam.stop_recording()
cam.stop_preview()


print('video le liya')
