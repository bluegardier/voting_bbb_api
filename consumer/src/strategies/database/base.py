from abc import ABC, abstractmethod
from typing import Dict


class DatabaseStrategy(ABC):
    @abstractmethod
    def insert_vote(self, vote_data: Dict): ...
