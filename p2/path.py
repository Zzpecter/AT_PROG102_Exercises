from abc import ABC, abstractmethod

class Path(ABC):
    @abstractmethod
    def getSpeed(self):
        pass