import socket
from fastapi import APIRouter, HTTPException, status
from app_utils.utils import return_request_metadata
from app_utils.queue_utils import send_to_queue
from schemas.voting_schema import VoteRecord
from src.utils.logger import default_logger

router = APIRouter(prefix="/voting")


async def register_vote(candidate: str):
    request_id, timestamp = return_request_metadata()
    hostname = socket.gethostname()

    vote = VoteRecord(
        request_id=request_id,
        timestamp=timestamp,
        arthur_aguiar=1 if candidate == "arthur" else 0,
        davi_brito=1 if candidate == "davi" else 0,
        yagami_light=1 if candidate == "yagami" else 0,
    )

    try:
        await send_to_queue(vote.model_dump_json())
    except Exception as e:
        default_logger.error(f"Error sending vote to {candidate}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unable to register vote for {candidate} at this time. Error: {e}",
        )

    return {
        "message": f"Vote successfully registered for {candidate.capitalize()}",
        "status_code": status.HTTP_200_OK,
        "request_id": request_id,
        "timestamp": timestamp.isoformat(),
        "container_id": hostname,
    }


@router.post("/arthur", status_code=status.HTTP_200_OK)
async def register_arthur():
    return await register_vote("arthur")


@router.post("/davi", status_code=status.HTTP_200_OK)
async def register_davi():
    return await register_vote("davi")


@router.post("/yagami", status_code=status.HTTP_200_OK)
async def register_yagami():
    return await register_vote("yagami")
