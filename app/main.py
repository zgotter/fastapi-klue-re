from typing import Dict
import pandas as pd
from fastapi import FastAPI
import torch
from app.model import load_tokenizer, load_model, inference
from app.load_data import load_dataset, num_to_label

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello": "world"}

@app.post("/predict", description="관계를 예측합니다.")
async def predict(data: dict):
    data_df = pd.DataFrame(data)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    tokenizer = load_tokenizer()
    model = load_model(device)
    dataset = load_dataset(data_df, tokenizer)
    pred_answer, _ = inference(model, dataset, device)
    answer = num_to_label(pred_answer)
    print("answer:", answer)
    return {"relation": answer[0]}