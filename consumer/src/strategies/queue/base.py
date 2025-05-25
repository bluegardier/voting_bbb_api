from abc import ABC, abstractmethod


class QueueStrategy(ABC):
    @abstractmethod
    def consume(self): ...
