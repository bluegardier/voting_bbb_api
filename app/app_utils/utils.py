import uuid
from datetime import datetime, timezone


def return_request_metadata():
    request_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc)
    return request_id, timestamp
