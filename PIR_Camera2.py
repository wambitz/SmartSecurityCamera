#CÓDIGO BASE
# Librerias
#import RPi.GPIO as GPIO
#import time
#import picamera

def system_on():

	#Modo de uso de GPIO
	# GPIO.setmode(GPIO.BCM)

	#Configuraciones iniciales
	# GPIO_PIR = 24
	# GPIO_LED=25
	# GPIO.setup(GPIO_PIR,GPIO.IN)
	# GPIO.setup(GPIO_LED,GPIO.OUT)
	# ValorPIR= 0

	#Ciclo
	#ValorPIR = GPIO.input(GPIO_PIR)
	while(ValorPIR == 0):
		time.sleep(.01)
		print "INTRUDER"
	with picamera.PiCamera() as picam:
		print "Taking picture"
		# picam.start_preview()
		# GPIO.output(GPIO_LED,GPIO.HIGH)
		# picam.capture('Intruso.jpg')
		# picam.stop_preview()
		# picam.close()
		# time.sleep(3)
		# GPIO.output(GPIO_LED,GPIO.LOW)
	#GPIO.cleanup()

