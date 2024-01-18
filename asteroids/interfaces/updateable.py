from abc import ABC
from abc import abstractmethod

from pygame import Surface

class Updateable(ABC):
    @abstractmethod
    def update(self, screen: Surface, dt: float) -> None:
        raise NotImplementedError() 
