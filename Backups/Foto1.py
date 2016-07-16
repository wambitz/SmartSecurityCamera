import time
import picamera

with picamera.PiCamera() as picam:
	picam.start_preview()
	picam.capture('python.jpg')
	picam.stop_preview()
	picam.close()