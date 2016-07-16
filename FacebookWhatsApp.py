"""FacebookWhatsApp messageFb messageW
    example messageFb: 'He\'s a complicated man. And the only one that understands him is his woman'
    example messageW: "Aqui tu mensaje"
    example pathFoto: 'electro.jpg'
"""    

from facepy import GraphAPI
import base64
#from Examples.EchoClient import WhatsappEchoClient             #Importa la Clase WhatsappEchoClient, dedicada a envio de mensajes.
from yowsup.src.Examples.EchoClient import WhatsappEchoClient   

oauth_access_token="CAACEdEose0cBALNZCku7OyE5xBM0vdrbaF4RKvQrIEwt7giZCtfeH04kgttq9smYgaHkmrZBdgwaw8rQhM8xxZBjzc1xGQCQXOoQeuNj6bSKCZCETlVg4zf6Hqy08i2OYonWeqRvmIICEEeI2C1QKnuvqF6ROHVA4KZAh46RSMs17jPaatl8Fz6HiczBZB4oqIZD"

def EnviarMensajeAFb(messageFb):        
    graph = GraphAPI(oauth_access_token)   
    graph.post(path='me/feed',message=messageFb)
    
def EnviarFotoAFb(pathFoto):    
    graph = GraphAPI(oauth_access_token)       
    graph.post(path = 'me/photos',source = open(pathFoto, 'rb'))

def EnviarMensajeAW(messageW):
    #................Clave de Acceso a WhatsApp............................
    password = "WIWnFS6AvXLP9tMd2M1Ltcibfuk="                      #Password dada al registrar el numero.
    password = base64.b64decode(bytes(password.encode('utf-8')))   #Codificacion de Password para envio a los servidores de whatsApp.
    username = '5219991780816'                                     #Numero de telefono para el inicio de secion.
    keepAlive= False                                               #Conexion persistente con el servidor.
    TelefonoDestino = "5219993389539"
    #......................................................................
    whats = WhatsappEchoClient(TelefonoDestino, messageW, keepAlive)  #Inicia el cliente para el envio de mensajes por WhatsApp.
    whats.login(username, password)                                   #Autentifica el dispositivo con el cliente de WhatsApp.