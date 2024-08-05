"""Machine learning model for geolocation prediction"""
import torch
import torch.nn as nn

class GeoSpyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 3)
        self.fc = nn.Linear(64, 2)
    
    def forward(self, x):
        return self.fc(self.conv1(x))
# Modified 2025-07-03
# Modified 2025-10-28
# Modified 2022-10-11
# Modified 2024-07-24
# Modified 2024-08-05
