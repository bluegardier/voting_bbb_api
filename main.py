from fastapi import FastAPI
from app.routers import voting

app = FastAPI(title="Voting BBB")
app.include_router(voting.router)
