import uvicorn
from fastapi import FastAPI
from routers import voting

app = FastAPI(title="Voting BBB")
app.include_router(voting.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
