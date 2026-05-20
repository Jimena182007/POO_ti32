class Silla:
    def __init__(self,material,color,tiene_respaldo,brazos, altura,peso, giratoria,ruedas, precio,estilo):
          self.material = material 
          self.color = color
          self.tiene_respaldo = tiene_respaldo
          self.brazos = brazos 
          self.altura = altura 
          self.peso = peso
          self.giratoria = giratoria 
          self.ruedas = ruedas
          self.precio = precio
          self.estilo = estilo 
          print (f"material:{self.material}")
          print (f"color:{self.color}")
          print (f"tiene_respaldo:{self.tiene_respaldo}")
          print (f"brazos:{self.brazos}")
          print (f"altura:{self.altura}")
          print (f"peso:{self.peso}")
          print (f"giratoria:{self.giratoria}")
          print (f"rueda:{self.ruedas}")
          print (f"precio:{self.precio}")
          print (f"estilo:{self.estilo}")

    def ajustarAltura(self):
        print("ajustar altura")
    def girar(self):
        print("girar")
    def reciclar(self):
        print("reciclar")
    def mover(self):
        print("mover")
    def soportarPeso(self):
        print("soportar peso")
silla=Silla("plastico","negro","esponja","largos","tres kilos","treinta grados","cuatro ruedas","trescientos","oficina")