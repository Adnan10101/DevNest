from fastapi import FastAPI
import uvicorn
from src.infra import Infra
from src.schema import(
    CreateInfraClaim
)
import src.env as env

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to devnest"}

@app.post("/test")
async def test(request: CreateInfraClaim):
    #try:
        req = Infra(env.INFRA_FILE_PATH, env.REPO_NAME)
        req.create_claim(request = request, claim = "infra_claim")
    #except Exception as e:
    #    return "Error, ",e 
        
if __name__ == "__main__":
    uvicorn.run("main:app", host = '0.0.0.0',port = 6001, log_level = "info")