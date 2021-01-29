#!/usr/bin/env python3

import sys


#------------------nou

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from transformers import AdamW

def read_data():
    file_path_to_input = "/Users/macbook/RubymineProjects/proiect_sac/public/uploads/" + str(sys.argv[1]) + "_files/output/testfile.txt"
    f = open(file_path_to_input, "r")
    return [f.read()]

def write_file(data):
    file_path_to_output = "/Users/macbook/RubymineProjects/proiect_sac/public/uploads/" + str(sys.argv[1]) + "_files/output/testfile2.txt"
    f = open(file_path_to_output, "w")
    f.write(str(data))

class BERT_Arch(nn.Module):

    def __init__(self, bert):
        super(BERT_Arch, self).__init__()

        self.bert = bert

        # dropout layer
        self.dropout = nn.Dropout(0.1)

        # relu activation function
        self.relu = nn.ReLU()

        # dense layer 1
        self.fc1 = nn.Linear(768, 512)

        # dense layer 2 (Output layer)
        self.fc2 = nn.Linear(512, 9)

        # softmax activation function
        self.softmax = nn.LogSoftmax(dim=1)

    # define the forward pass
    def forward(self, sent_id, mask):
        # pass the inputs to the model
        _, cls_hs = self.bert(sent_id, attention_mask=mask)

        x = self.fc1(cls_hs)

        x = self.relu(x)

        x = self.dropout(x)

        # output layer
        x = self.fc2(x)

        # apply softmax activation
        x = self.softmax(x)

        return x

# import BERT-base pretrained model
bert = AutoModel.from_pretrained('dumitrescustefan/bert-base-romanian-cased-v1')

# Load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("dumitrescustefan/bert-base-romanian-cased-v1")

device = torch.device('cpu')

model2 = BERT_Arch(bert)

optimizer = AdamW(model2.parameters(), lr = 1e-3)

path = 'app/assets/python/data/saved_weights.pt'
model2.load_state_dict(torch.load(path, map_location=device))
model2.eval()
model2 = model2.cpu()

sec_text = read_data()

max_seq_len = 256

tokens_test = tokenizer.batch_encode_plus(
    sec_text,
    max_length = max_seq_len,
    pad_to_max_length=True,
    truncation=True,
    return_token_type_ids=False
)

# for test set
test_seq = torch.tensor(tokens_test['input_ids'])
test_mask = torch.tensor(tokens_test['attention_mask'])
# test_y = torch.tensor(test_labels.tolist())

with torch.no_grad():
  preds = model2(test_seq.cpu(), test_mask.cpu())
  preds = preds.numpy()

preds = np.argmax(preds, axis = 1)
preds += 2
write_file(preds[0])