class Coche:
    def __init__(self,marca,modelo,color,año,placas,num_puertas,kilometraje,tipo_conbustible,automatico,precio):
          self.marca = marca 
          self.modelo = modelo
          self.color = color
          self.año = año 
          self.placas = placas 
          self.num_puertas = num_puertas
          self.kilometraje = kilometraje 
          self.tipo_conbustible = tipo_conbustible
          self.automatico = automatico
          self.precio = precio 
          print (f"marca:{self.marca}")
          print (f"modelo:{self.modelo}")
          print (f"color:{self.color}")
          print (f"año:{self.año}")
          print (f"placas:{self.placas}")
          print (f"num_puertas:{self.num_puertas}")
          print (f"kilometraje:{self.kilometraje}")
          print (f"tipo_combustible:{self.tipo_combustible}")
          print (f"automatico:{self.automatico}")
          print (f"precio:{self.precio}")

    def encender(self):
        print("encender")
    def acelerar(self):
        print("acelera")
    def frenar(self):
        print("frena")
    def tocaClaxon(self):
        print("toca el claxon")
    def transporta(self):
        print("te lleva a un lugar")
mustang=Coche("mustang","2026","rojo","2026","TESDRT6AD","cuatro_puertas","00002","disel","estandar","un millon")