#CÓDIGO BASE
# Librerias
import RPi.GPIO as GPIO
import time
import picamera

#Modo de uso de GPIO
GPIO.setmode(GPIO.BCM)

#Configuraciones iniciales
GPIO_PIR = 24
GPIO.setup(GPIO_PIR,GPIO.IN)
ValorPIR= 0

#Ciclo
try:
	while True:
		ValorPIR = GPIO.input(GPIO_PIR)
		if  (ValorPIR == 1):
			print "INTRUDER"
			with picamera.PiCamera() as picam:
				print "Taking picture"
				picam.start_preview()
				picam.capture('Intruso.jpg')
				picam.stop_preview()
				picam.close()
			print "Sleeping 10s"
			time.sleep(10)
		else:
			print "No intruder"
			time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()

