from Personaje.Personaje.InterfaceAdapter import InterfaceAdapter
from Personaje.Personaje.jugador import Personaje


class Character(InterfaceAdapter):
    __player = Personaje()

    def piupiu(self,x,y):
        self.__player .disparar(x,y)
        pass

    def move(self):
        self.__player.mover()
        pass

    def addCharacter(self,screen):
        self.__player.dibujar(screen)

    def getArrayDisparo(self):
        return self.__player.listaDisparo

    def getRecorrido(self):
        return self.__player