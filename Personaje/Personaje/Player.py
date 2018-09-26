class Player:
    __playerSprite = ""
    __disparoSprite = ""
    __sound = ""

    def __init__(self,player,disparo,sound):
        self.__sound = sound
        self.__disparoSprite = disparo
        self.__playerSprite = player

    def getSprite(self):
        return self.__playerSprite
    def getDisparo(self):
        return self.__disparoSprite
    def getSound(self):
        return self.__sound