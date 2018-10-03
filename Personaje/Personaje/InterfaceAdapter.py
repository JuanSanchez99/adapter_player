from abc import ABCMeta, abstractmethod

class InterfaceAdapter():

    __metaclass__ = ABCMeta

    @abstractmethod
    def piupiu(self):pass

    @abstractmethod
    def move(self):pass

    @abstractmethod
    def addCharacter(self):pass
