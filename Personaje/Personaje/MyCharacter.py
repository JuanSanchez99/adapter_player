from Personaje.Personaje.InterfaceAdapter import InterfaceAdapter
from Personaje.Personaje.jugador import Personaje


class Character(InterfaceAdapter, Personaje):

    def __init__(self):
        Personaje.__init__(self)

    def piupiu(self, x, y):
        self.disparar(x,y)

    def move(self):
        self.mover()

    def addCharacter(self, screen):
        self.dibujar(screen)