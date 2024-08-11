import torch
from torch import nn
import pytorch_lightning as pl
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from src.data.preprocessing import map_susp_cobranza
from torchvision import transforms



class CarteraDataset(Dataset):
    def __init__(self, X,y):  
        self.X = torch.FloatTensor(X)
        self.y = torch.FloatTensor(y)
    
    def __len__(self):
        return len(self.y)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
    

class CarteraDataLoader(pl.LightningDataModule):
    def __init__(self, X,y, batch_size=32):
        super().__init__()
        self.X = X
        self.y = y
        self.batch_size = batch_size

    def setup(self, stage=None):
        dataset = CarteraDataset(self.X, self.y)
        train_size = int(0.8 * len(dataset))
        val_size = len(dataset) - train_size
        self.train_dataset, self.val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)


class BinaryClassificationModel(pl.LightningModule):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.layer2 = nn.Linear(hidden_dim, hidden_dim)
        self.layer3 = nn.Linear(hidden_dim, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)
    
    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.dropout(x)
        x = self.relu(self.layer2(x))
        x = self.dropout(x)
        return torch.sigmoid(self.layer3(x))
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = nn.BCELoss()(y_hat, y.unsqueeze(1))
        
        predictions = (y_hat > 0.5).float()
        accuracy = (predictions == y.unsqueeze(1)).float().mean()
        
        self.log('train_loss', loss)
        self.log('train_accuracy', accuracy)
        
        return loss
    
    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = nn.BCELoss()(y_hat, y.unsqueeze(1))
        
        predictions = (y_hat > 0.5).float()
        accuracy = (predictions == y.unsqueeze(1)).float().mean()
        
        self.log('val_loss', loss)
        self.log('val_accuracy', accuracy)
        
        return loss
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)


