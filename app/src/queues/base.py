from abc import ABC, abstractmethod
from typing import Dict


class QueueService(ABC):
    @abstractmethod
    async def send(self, data: Dict):
        "Send data to a queue"
        ...
