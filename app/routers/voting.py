from app.app_utils.utils import return_request_metadata
from fastapi import APIRouter
from schemas.voting_schema import VoteRecord

router = APIRouter(prefix="/voting")

@router.post("/arthur")
async def register_arthur():
    request_id, timestamp = return_request_metadata()
    vote = VoteRecord(
        request_id=request_id,
        timestamp=timestamp,
        arthur_aguiar=1,
        davi_brito=0,
        yagami_light=0
    )
    # send_to_queue(vote.dict())
    return {
        "message": "Voto Registrado para Arthur",
        "status_code": 200
        }

@router.post("/davi")
async def register_davi():
    request_id, timestamp = return_request_metadata()
    vote = VoteRecord(
        request_id=request_id,
        timestamp=timestamp,
        arthur_aguiar=0,
        davi_brito=1,
        yagami_light=0
    )
    # send_to_queue(vote.dict())
    return {
        "message": "Voto Registrado para Davi",
        "status_code": 200
        }
    
@router.post("/yagami")
async def register_yagami():
    request_id, timestamp = return_request_metadata()
    vote = VoteRecord(
        request_id=request_id,
        timestamp=timestamp,
        arthur_aguiar=0,
        davi_brito=0,
        yagami_light=1
    )
    # send_to_queue(vote.dict())
    return {
        "message": "Voto Registrado para Yagami",
        "status_code": 200
        }
    