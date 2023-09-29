class Notificador:
    def __init__(self, usuario, mensaje):    
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificacionEmail(Notificador):
    def Notificar(self):
        print("Enviando un mensaje por email a {self.usuario.email}")
                    
class NotificacionSms(Notificador):
    def Notificar(self):
        print("Enviando un mensaje por sms a {self.usuario.sms}")

class NotificacionWhatsApp(Notificador):
    def Notificar(self):
        print("Enviando un mensaje por WhatsApp a {self.usuario.whatsapp}")