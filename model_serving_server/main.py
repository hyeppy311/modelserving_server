from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import requests
import json
import sys
import os
from starlette.config import Config

config = Config('.env')
API_TOKEN = config('API_TOKEN')
headers = {"Authorization": f"Bearer {API_TOKEN}"}

app = FastAPI()


# inputdata 설정
class ModelInfer(BaseModel) :
    id : Optional[str] = None
    parameters : Optional[str] = None
    data :  dict

# Health 
# live : 애플리케이션과 서빙모델 연결 상태
@app.get("/v2/models/{model_name}/live/")
async def server_ready(model_name) :
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    response = requests.get(API_URL)
    
    if response.status_code == 200 :
        return "Sucess to connect model server"
    else :  
        return "Fail to connect model server"

# ready : 애플리케이션 초기화 후 모델 서버 다시 로드 후 
@app.get("/v2/models/{model_name}/ready/")
async def get_model_live(model_name: str):

    return {"model_name": model_name, "status": "live"}

# 서버메타데이터 
@app.get("/v2/")
async def server_metadata():
    server_metadata = {
                    "name" : 'Model_serving_server',
                    "version" : '1.0.0'
                        }
    return server_metadata

# 모델 메타데이터 / version 입력
@app.get("/v2/models/{model_name}/")
async def model_metadata(model_name) :
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    response = requests.get(API_URL) 
    
    if response.status_code == 200: 
        model_metadata = response.json()["cardData"]
        return model_metadata
    else : 
        return "fail"

# 서빙 api

@app.post("/v2/models/{model_name}/versions/{model_version}/infer")
async def model_serving(model_name, model_version, model : ModelInfer):
    input = model.data
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    response = requests.request("POST",API_URL, headers=headers, data=input)
    outputs = json.loads(response.content.decode("utf-8"))
    
    return {"model_name":model_name, "version": model_version, "input": input, "output":outputs}