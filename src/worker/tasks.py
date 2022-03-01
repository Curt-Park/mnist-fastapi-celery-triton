# -*- coding: utf-8 -*-
"""Producer."""
import torch
from PIL import Image

from ml.dataloader import get_preprocessor
from worker.predictor import BasePredictor, Predictor, PredictorTriton

from .celery import app

preprocess = get_preprocessor()
predictors = {"NAIVE": BasePredictor(), "TRITON": PredictorTriton()}


def get_image(image_name: str) -> torch.FloatTensor:
    """Preprocess the image."""
    image = Image.open(image_name)
    image = torch.unsqueeze(preprocess(image), 0)
    return image


@app.task
def predict_digit(image_name: str) -> int:
    """Predict a handwritten digit image."""
    # lazy init for sementation annotator
    # celery doesn't support spawn, but pytorch only supports spawn
    # https://github.com/celery/celery/issues/6036
    if isinstance(predictors["NAIVE"], BasePredictor):
        predictors["NAIVE"] = Predictor()

    try:
        image = get_image(image_name)
        prediction = predictors["NAIVE"].predict(image)
    except FileNotFoundError:
        prediction = -1
    return prediction


@app.task
def predict_digit_triton(image_name: str) -> int:
    """Predict a handwritten digit image with Triton."""
    try:
        image = get_image(image_name)
        prediction = predictors["TRITON"].predict(image)
    except FileNotFoundError:
        prediction = -1
    return prediction
