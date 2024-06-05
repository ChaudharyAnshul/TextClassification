from transformers import BertForSequenceClassification, BertTokenizer
import torch
import pickle

class BertClassifierModel:
  def __init__(self):
    # Initialize BERT model and tokenizer
    model_name = '../models/bert_custom_1'
    self.model = BertForSequenceClassification.from_pretrained(model_name)
    self.tokenizer = BertTokenizer.from_pretrained(model_name)
    
    # device
    self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    self.model.to(self.device)
    
    # label encoder
    with open('../models/encoder_model.pkl', 'rb') as f:
      self.label_encoder = pickle.load(f)

  def predict(self, text):
    # Tokenize input text
    inputs = self.tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    
    inputs = {k: v.to(self.device) for k, v in inputs.items()}
    
    # Make prediction
    with torch.no_grad():
      outputs = self.model(**inputs)
    predicted_labels = torch.argmax(outputs.logits, dim=-1).cpu().tolist()
    
    # decode label
    res = self.label_encoder.inverse_transform(predicted_labels)
    
    return res[0]