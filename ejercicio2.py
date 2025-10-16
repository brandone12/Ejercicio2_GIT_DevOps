class Figura:
  def dibujar(self):
    return "Dibujando figura"

class Circulo:
  def dibujar(self):
    return "Círculo dibujado"

class Cuadrado:
  def dibujar(self):
    return "Cuadrado dibujado"

figuras = [Circulo(), Cuadrado()]

for figura in figuras:
  print(figura.dibujar())