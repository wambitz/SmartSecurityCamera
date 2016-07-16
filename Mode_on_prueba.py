import time
for i in range(0, 5):
	print "LEDs encendidos"
	for j in range (0, 5):
		print "foto" + str(j) + ".jpg"
		time.sleep(1)
	# end for j
	print "Envio por mail"
	print "Mensaje fb"
	print "Mensaje whatsapp"
	print "Apagar LEDs"
	time.sleep(5)
#end for i
	