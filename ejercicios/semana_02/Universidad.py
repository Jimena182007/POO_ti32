class Universidad:
    def __init__(self,nombre, ubicación,alumnos,carreras,año_fundacion,rector, presupuesto,biblioteca,graduacion_alumnos):
          self.nombre = nombre
          self.ubicación = ubicación 
          self.alumnos = alumnos 
          self.carreras = carreras
          self.año_funcion = año_funcion
          self.rector = rector
          self.presupuesto = presupuesto
          self.biblioteca = biblioteca 
          self.graduacion_alumno = graduacion_alumnos
          print (f"nombre:{self.nombre}")
          print (f"ubicacionón:{self.ubicacion}")
          print (f"alumnas:{self.alumnas}")
          print (f"carreras:{self.carreras}")
          print (f"año_fundacion:{self.año_fundacion}")
          print (f"rector:{self.resctor}")
          print (f"presupuesto:{self.presupuesto}")
          print (f"biblioteca:{self.biblioteca}")
          print(f"graduación_alumnos:{self.graduacion_alumnos}")
    def incribirAlumno(self):
        print("inscribir alumno")
    def contratarProfesor(self):
        print("contratar profesor")
    def abrirCarreras(self):
        print("abrir carreras")
    def dasrBecas(self):
        print("dar becas")
    def graduarAlumnos(self):
        print("graduar alumnos")
    
unam=Universidad ("unam","felipe angeles","trecientos alumnos","contac,diseño,medicina,emfermeria,robotica,etc","1986","agustin","un millón trecientos","tres bibliotecas","50 generaciones graduadas")