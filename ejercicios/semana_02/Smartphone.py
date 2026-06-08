class Smartphone:
    def __init__(self,marca,modelo,color,tamaño, almacenamiento,ram,bateria,camara, sistema_operativo,precio):
          self.marca = marca
          self.modelo = modelo 
          self.color = color
          self.tamaño = tamaño
          self.almacenamiento = almacenamiento 
          self.ram = ram 
          self.bateria = bateria
          self.camara = camara
          self.sistema_operativo = sistema_operativo
          self.precio = precio 
          print (f"marca:{self.marca}")
          print (f"modelo:{self.modelo}")
          print (f"color:{self.color}")
          print (f"tamaño:{self.tamaño}")
          print (f"almacenamiento:{self.almacenamiento}")
          print (f"ram:{self.ram}")
          print (f"bateria:{self.bateria}")
          print (f"camara:{self.camara}")
          print (f"sistema_operativo:{self.sistema_operativo}")
          print (f"precio:{self.precio}")
          
    def llamar(self):
        print("llamar")

    def emviaMensajes(self):
        print("emvia mensajes")

    def tomaFotos(self):
        print("tomar fotos")

    def intalaApps(self):
        print("intala apps")

    def cargarBateria(self):
        print("cargar bateria")

Smartphone=Smartphone ("iPhone","15","negro","1.5","16 gigas","16","100","4k","once mil")
     

