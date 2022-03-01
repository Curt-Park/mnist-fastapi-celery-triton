#!/bin/sh
echo "Training starts"
PYTHONPATH=src/ml python src/ml/train.py
echo "The trained model is save as model.pt"
mkdir -p model_repository/mnist_cnn/1
cp model.pt model_repository/mnist_cnn/1
echo "model.pt is copied to model_repository/mnist_cnn/1"
