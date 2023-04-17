from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):

  _listaFutbolistas=[]
  def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
    self._golesMarcados=golesMarcados
    self._tarjetasRojas=tarjetasRojas
    self._piernaHabil=piernaHabil
    Persona.__init__(self,nombre,edad,altura,sexo)
    Deportista.__init__(self,añosPracticando)
    Futbolista._listaFutbolistas.append(self)


  @classmethod
  def setListaFutbolistas(cls,listaFutbolistas):
    cls._listaFutbolistas=listaFutbolistas
  @classmethod
  def getListaFutbolistas(cls):
    return cls._listaFutbolistas

  def setPiernaHabil(self,piernaHabil):
    self._piernaHabil=piernaHabil
  def getPiernaHabil(self):
    return self._piernaHabil

  def setTarjetasRojas(self,tarjetasRojas):
    self._tarjetasRojas=tarjetasRojas
  def getTarjetasRojas(self):
    return self._tarjetasRojas

  def getGolesMarcados(self):
    return self._golesMarcados
  def setGolesMarcados(self,golesMarcados):
    self._golesMarcados=golesMarcados

  def __str__(self):
    return f'Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte'
