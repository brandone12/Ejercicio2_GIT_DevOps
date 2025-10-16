class Notificacion:
  def enviar(self):
    return "Notificación enviada"

class Correo:
  def enviar(self):
    return "Correo enviado"

class SMS:
  def enviar(self):
    return "SMS enviado"

class Push:
  def enviar(self):
    return "Push enaviado"

def enviar_notificacion(objeto):
  print(objeto.enviar())

correo = Correo()
sms = SMS()
push = Push()

enviar_notificacion(correo)
enviar_notificacion(sms)
enviar_notificacion(push)