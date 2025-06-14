from fastapi import FastAPI
import uvicorn
from src.infra import Infra
from src.schema import(
    CreateInfraClaim,
    CreateCloudClaim
)
from src.template import (
     infra_claim,
     cloud_claim
)
import src.env as env

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to devnest"}

@app.post("/virtInfra", tags = ["virtual"])
async def create_virtual_claim(request: CreateInfraClaim):
    req = Infra(env.INFRA_FILE_PATH, env.REPO_NAME, infra_claim)
    req.create_claim(request = request)

@app.post("/cloudInfra", tags = ["cloud"])
async def create_cloud_infra(request: CreateCloudClaim):
    req = Infra(env.CLOUD_FILE_PATH, env.REPO_NAME, cloud_claim)
    req.create_cloud(request)
        
if __name__ == "__main__":
    uvicorn.run("main:app", host = '0.0.0.0',port = 6001, log_level = "info")