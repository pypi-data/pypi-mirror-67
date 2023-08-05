#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Dataset
While there are so many good packages, the purposes of this doc
is to focus on other changes and leave dataset loading stuff here
and then forget it.

This file should support all datasets we need to use again and again.
It is not mandatory to use it, i hope it will save time to use this.

Note that, these methods should make the transition between colab and 
local envs easy for user.

There is no need to make a generic functinos, just ones for our use case.

"""
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST, CIFAR10
from os.path import join


class ds():
    def __init__(self, base_path):
        super().__init__()
        assert len(base_path) > 0, "Base path should not be empty."
        self.base_path = base_path

    def mnist(self, transforms, train_prefix='mnist/train', test_prefix='mnist/test'):
        _path_train = join(self.base_path, train_prefix)
        _path_test = join(self.base_path, train_prefix)
        train_set = DataLoader(
            MNIST(_path_train, download=True, train=True, transform=transforms))
        test_set = DataLoader(
            MNIST(_path_test, download=True, train=False, transform=transforms))

        X_train = train_set.dataset.data.to(
            dtype=torch.float32).view(-1, 1, 28, 28)
        y_train = train_set.dataset.targets.to(dtype=torch.long)

        X_test = test_set.dataset.data.to(
            dtype=torch.float32).view(-1, 1, 28, 28)
        y_test = test_set.dataset.targets.to(dtype=torch.long)

        return X_train, y_train, X_test, y_test

    def cifar10(self, train_prefix='cifar10/train', test_prefix='cifar10/test'):
        _path_train = join(self.base_path, train_prefix)
        _path_test = join(self.base_path, train_prefix)
        train_set = DataLoader(
            CIFAR10(_path_train, download=True, train=True, transform=transforms))
        test_set = DataLoader(
            CIFAR10(_path_test, download=True, train=False, transform=transforms))

        return None
        # X_train = train_set.dataset.data.to(
        #     dtype=torch.float32).view(-1, 1, 28, 28)
        # y_train = train_set.dataset.targets.to(dtype=torch.long)

        # X_test = test_set.dataset.data.to(
        #     dtype=torch.float32).view(-1, 1, 28, 28)
        # y_test = test_set.dataset.targets.to(dtype=torch.long)

        # return X_train, X_test, y_train, y_test
    def dibetes():
        pass
