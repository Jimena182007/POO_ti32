class Persobaje_juego:
    def __init__(self,nombre,nivel,vida,energia,fuerza,defensa,velocidad,arma,skin,puntos_extra):
          self.nombre = nombre
          self.nivel = nivel 
          self.vida = vida
          self.energia = energia 
          self.fueeza = fuerza 
          self.defensa = defensa 
          self.velocidad = velocidad
          self.arma = arma
          self.skin = skin 
          self.puntos_extra = puntos_extra 
          print  (f"nombre:{self.nombre}")
          print  (f"nivel:{self.nivel}")
          print  (f"vida:{self.vida}")
          print  (f"energia:{self.energia}")
          print  (f"fuerza:{self.fuerza}")
          print  (f"velocidad:{self.velocidad}")
          print  (f"arma:{self.arma}")
          print  (f"skin:{self.skin}")
          print  (f"puntos_extra:{self.puntos_extras}")
 
    def atacar(self):
        print("atacar al resto de los jugadores ")
    def defender(self):
        print("defender")
    def saltar(self):
        print ("saltar opstaculos")
    def ganarPuntos(