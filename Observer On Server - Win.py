from flask import Flask, request, session, redirect, url_for, \
				 render_template, flash
#import time, picamera
from emailer import sendMail
from flask_mail import Mail, Message
from FacebookWhatsApp import EnviarMensajeAFb, EnviarFotoAFb, EnviarMensajeAW
#from PIR_Camera2 import system_on
#import subprocess
#import RPi.GPIO as GPIO 
import time


# Mail configuration
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT =  465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'observer.on.server@gmail.com'
MAIL_PASSWORD = 'ObserverOnServer'
DEFAULT_MAIL_SENDER = 'observer.on.server@gmail.com'

# App Configuration
SECRET_KEY = 'Development key'
USERNAME = 'admin'
PASSWORD = 'default'
	
app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

###### VIEW URLS ######

# Home page
@app.route("/")
def index():
	# subprocess.call("./ShellScripts/stop_raspivid.sh")
	return render_template('home.html')
	
@app.route("/services")
def services():
	# subprocess.call("./ShellScripts/stop_raspivid.sh")
	return render_template('services.html')
	
@app.route("/about")
def about():
	return render_template('about.html')
	
###### SESSION & CONTACT ######
	
# Session Log in	
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username']!= app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('index'))
	return render_template('login.html', error=error)
	
#Log out function	
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('index'))
	
# Contact - Mail send	
@app.route("/contact",  methods = ['GET' , 'POST' ])
def contact():
	if request.method == 'POST':
		message = request.form['txtArea']
		email = request.form['eMail']
		sendMail(email, message)
		#flash('Message sent')
	return render_template('contact.html')
	
###### TESTINGS ######
	
# Send Photo to Mail
@app.route("/attachpic", methods=['GET', 'POST'])
def attachpic():
	if request.method == 'POST':
		usermail = (request.form['usermail'])
		msg = Message('Testing', 
					sender = app.config['MAIL_USERNAME'],
					recipients = [usermail])
		with app.open_resource('static/_images/python.jpg') as pic:
			msg.attach('python.jpg', 'image/jpg', pic.read())
		mail.send(msg)
		return redirect(url_for('take_pic'))
		
# Test E-mail
@app.route('/mail', methods=['GET', 'POST'])
def sendmail():
	function = 'Sending E-mail'
	mode = 'mail'
	templateData = {
		'function' : function,
		'mail'  : mode
	}
	if request.method == 'POST':
		usermail = request.form['email']
		message = request.form['message']
		msg = Message(message, 
					sender = app.config['MAIL_USERNAME'],
					recipients = [usermail])
		mail.send(msg)
	return render_template('testing.html',**templateData)
	
# Take picture function	
@app.route("/camera")
def take_pic():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function = 'Taking picture'
	mode = 'picture'
#	with picamera.PiCamera() as picam:
	#	picam.start_preview()
	#	time.sleep(5)
	#	picam.capture('python.jpg')
	#	picam.stop_preview()
	#	picam.close()
	templateData = {
		'function' : function,
		'picture'  : mode
	}
	return render_template('testing.html', **templateData)	
	
# Stream video function
@app.route("/video")
def stream():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "Streaming Video"
	mode = 'stream'
	templateData = {
		'function' : function,
		'stream'   : mode
	}
	#subprocess.call("./ShellScripts/start_raspivid.sh")
	return render_template('testing.html', **templateData)

# Facebook Post 
@app.route("/fb",  methods=['GET', 'POST'])
def fb():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "Facebook Post"
	mode = 'fb'
	templateData = {
		'function' : function,
		'fb'   : mode
	}
	if request.method == 'POST':
		fbmsg = request.form['fbmsg']
		EnviarMensajeAFb(fbmsg)
	return render_template('testing.html', **templateData)

# Facebook Post Image
@app.route("/fbimg", methods=['GET', 'POST'])
def fbimg():
	if request.method == 'POST':
		EnviarFotoAFb('static/_images/python.jpg')
		return redirect(url_for('fb'))

# Whatsapp Message 
@app.route("/wa", methods=['GET', 'POST'])
def wa():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "WhatsApp Message"
	mode = 'wa'
	templateData = {
		'function' : function,
		'wa'   : mode
	}
	if request.method == 'POST':
		wamsg = str(request.form['wamsg'])
		EnviarMensajeAW(wamsg)
	return render_template('testing.html', **templateData)
	

@app.route("/LED")
def led_on():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "LED on"
	mode = 'led'
	templateData = {
		'function' : function,
		'led'   : mode
	}
	# GPIO.setmode(GPIO.BCM)
	# GPIO.setup(25, GPIO.OUT)
	# n = 0 
	# while (n<1):
		# GPIO.output(25, GPIO.HIGH)
		# time.sleep(5)
		# n = n + 1
		# print "Light On"
	# GPIO.output(25, GPIO.LOW)
	# print "Light Off"
	# GPIO.cleanup()
	return render_template('testing.html', **templateData)
	
@app.route("/PIR")
def PIR():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "Sensor"
	mode = 'PIR Probe'
	templateData = {
		'function' : function,
		'PIR'   : mode
	}
	# GPIO.setmode(GPIO.BCM)
	# GPIO.setup(24, GPIO.IN)
	# GPIO.setup(25, GPIO.OUT)	
	# n = 0
	# while (n<3):
		# if (GPIO.input(24)):
			# GPIO.output(25, GPIO.HIGH)
			# n = n + 1
			# time.sleep(.1)
		# else:
			# print "No sensing" # Try to break loop after a certain period of time
			# GPIO.output(25, GPIO.LOW)
			# time.sleep(.1)
	# GPIO.output(25, GPIO.LOW)
	# GPIO.cleanup()
	return render_template('testing.html', **templateData)

###### SURVEILLANCE/SECURITY MODE ON ######	
@app.route("/mode-on")
def mode_on():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "SYSTEM ON"
	mode = 'SYSTEM ON'
	templateData = {
		'function' : function,
		'mode_on'   : mode
	}
	# GPIO.setmode(GPIO.BCM)
	# GPIO.setup(24, GPIO.IN)
	# GPIO.setup(25, GPIO.OUT)
	# if (GPIO.input(24)):
		for i in range(0, 5):
			# GPIO.output(25, GPIO.HIGH)
			print "LEDs encendidos"			
			for j in range (0, 5):
				# picam.capture('foto' + str(j) + '.jpg')
				print "foto" + str(j) + ".jpg"
				time.sleep(1)
			# end for j
			print "Envio por mail"
			# EnviarMensajeAFb('Alerta! Hay un intruso!')
			print "Mensaje fb"
			# EnviarMensajeAW('Alerta! Hay un intruso!')
			print "Mensaje whatsapp"
			# GPIO.output(25, GPIO.LOW)
			print "Apagar LEDs"
			time.sleep(5)
			# time.sleep(20) # wait 20s before take another pic 
		# end for i	
		# GPIO.cleanup()
	return render_template('testing.html', **templateData)

@app.route("/mode-off")
def mode_off():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	function =  "SYSTEM OFF"
	mode = 'SYSTEM OFF'
	templateData = {
		'function' : function,
		'mode_off'   : mode
	}
	return render_template('testing.html', **templateData)
	
	
if (__name__) == ('__main__'):
	app.run(host='0.0.0.0', debug=True, port=81)
