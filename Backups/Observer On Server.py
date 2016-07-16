from flask import Flask, request, session, redirect, url_for, \
				 render_template, flash
#import time, picamera
from emailer import sendMail
from flask_mail import Mail, Message

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
	return render_template('home.html')
	
@app.route("/services")
def services():
	return render_template('services.html')
	
@app.route("/about")
def about():
	return render_template('about.html')
	
###### SESSION URLS ######
	
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
	
###### SERVICES URLS ######
	
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
	return render_template('testing.html', **templateData)


@app.route("/gallery")
def gallery():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	gallery = "Presenting Photo Gallery"
	return render_template('home.html', gallery=gallery)
	
@app.route("/test")
def test():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	test = "Testing"
	return render_template('home.html',test=test)
	
if (__name__) == ('__main__'):
	app.run(host='0.0.0.0', debug=True, port=80
	)
