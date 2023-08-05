"""
# The authors stated
# that the network being used was Keras MNIST CNN.
# The structure of this network can be found in the following
# link: https: // keras.io/examples/mnist_cnn/
# Function to apply Glorot Initialization on the netowrk
"""
from torch import nn
import torch


def weight_init(m):
    if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
        torch.nn.init.xavier_uniform_(
            m.weight, gain=nn.init.calculate_gain('relu'))
        torch.nn.init.zeros_(m.bias)


class MNIST_CNN(nn.Module):
    def __init__(self,):
        super(MNIST_CNN, self).__init__()
        self.convs = nn.Sequential(
            nn.Conv2d(1, 32, 3),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Dropout(0.25)
        )
        self.convs.apply(weight_init)
        self.fcs = nn.Sequential(
            nn.Linear(12*12*64, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 10),
        )
        self.fcs.apply(weight_init)

    def forward(self, x):
        out = x
        out = self.convs(out)
        out = out.view(-1, 12*12*64)
        out = self.fcs(out)
        return out
