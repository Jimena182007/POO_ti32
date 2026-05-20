class Mesa:
    def __init__(self,materiales,color,altura,ancho,largo,forma,peso,num_patas,precio,pegable):
          self.materiales = materiales
          self.color = color
          self.altura = altura 
          self.ancho = ancho 
          self.forma = forma 
          self.peso = peso
          self.num_patas = num_patas
          self.precio = precio
          self.pegable = pegable
          print (f"materiales:{self.materiales}")
          print (f"color:{self.color}")
          print (f"altura:{self.altura}")
          print (f"ancho:{self.ancho}")
          print (f"largo:{self.largo}")
          print (f"forma:{self.forma}")
          print (f"peso:{self.peso}")
          print (f"num_patas:{self.num_patas}")
          print (f"precio:{self.precio}")
          print (f"pegable:{self.pegable}")

    def soportarPeso(self):
        print("soportarPeso")
    def extender(self):
        print("extender")
    def limpiar(self):
        print("limpiar")
    def mover(self):
        print("mover")
    def cambiarAltura(self):
        print("cambiarAltura")
mesa=Mesa("madera","cafe","un metro",None,None,"rectangular","diez kilos","cuatro pata","seis mil pesos","no pegable")

