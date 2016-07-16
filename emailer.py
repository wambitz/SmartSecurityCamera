import smtplib
from email.mime.text import MIMEText

def sendMail(subject, body):
        myAdress = "observer.on.server@gmail.com"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = myAdress
        msg['Reply-to'] = myAdress
        msg['To'] = myAdress

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(myAdress, 'ObserverOnServer')
        server.sendmail(myAdress, myAdress, msg.as_string())
        server.quit()