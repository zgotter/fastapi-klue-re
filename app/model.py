import streamlit as st
import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoConfig, AutoModelForSequenceClassification

model_name = "klue/roberta-large"

def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer

def load_model(device):
    model_config = AutoConfig.from_pretrained(model_name)
    model_config.num_labels = 30

    model = AutoModelForSequenceClassification.from_pretrained(model_name, config=model_config)
    model.to(device)

    return model    

def inference(model, dataset, device):
  dataloader = DataLoader(dataset, batch_size=16, shuffle=False)
  model.eval()
  output_pred = []
  output_prob = []
  for i, data in enumerate(dataloader):
    with torch.no_grad():
      outputs = model(
          input_ids=data['input_ids'].to(device),
          attention_mask=data['attention_mask'].to(device),
          token_type_ids=data['token_type_ids'].to(device)
          )
    logits = outputs[0]
    prob = F.softmax(logits, dim=-1).detach().cpu().numpy()
    logits = logits.detach().cpu().numpy()
    result = np.argmax(logits, axis=-1)

    output_pred.append(result)
    output_prob.append(prob)
  
  return np.concatenate(output_pred).tolist(), np.concatenate(output_prob, axis=0).tolist()

