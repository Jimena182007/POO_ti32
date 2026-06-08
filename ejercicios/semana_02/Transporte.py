class Transporte:
    def __unit__(self,tipo_carro,capacidad,velocidad, combustible,color, año,num_puertas,placas,rutas,servicio):
          self.tipo_carro = tipo_carro
          self.capacidad = capacidad 
          self.velocidad = velocidad 
          self.combustuble = combustible
          self.color = color
          self.año = año
          self.num_puertas = num_puertas
          self.placas = placas
          self.rutas = rutas
          self.servicio = servicio 
          print (f"tipo_coche:{self.tipo_coche}")
          print (f"capacidad:{self.capacidad}")
          print (f"velocidad:{self.velocidad}")
          print (f"combustible:{self.combustible}")
          print (f"color:{self.color}")
          print (f"año:{self.año}")
          print (f"num_ruedas:{self.num_ruedas}")
          print (f"placas:{self.placas}")
          print(f"rutas:{self.rutas}")
          print (f"servicio:{self.servicio}")
    def arracar(self):
        print("arrancar veiculo")
    def frenar(self):
        print("frenar veiculo")
    def transportar(self):
        print("transportar pasajeros")
    def acelerar(self):
        print("acelerar")
    def detenerce(self):
        print("detenerce")
    
coche=Transporte ("chevi","hasta diez personas","gasolina","rojo","2025","cuatro","hjr7qbr","todas","personal")