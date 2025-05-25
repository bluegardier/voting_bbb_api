from src.queues.factory import get_queue_service
from src.core.config import QUEUE_BACKEND

queue_service = get_queue_service(QUEUE_BACKEND)


async def send_to_queue(data: dict):
    await queue_service.send(data)
