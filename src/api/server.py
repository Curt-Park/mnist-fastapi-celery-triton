# -*- coding: utf-8 -*-
"""API server that accepts requests and returns values."""
from fastapi import FastAPI

from worker.tasks import predict_digit, predict_digit_triton

app = FastAPI()


@app.get("/")
def root() -> str:
    """Show the proper usage."""
    return "Try api-address:8000/predict/image_name"


@app.get("/predict")
def predict_without_image() -> str:
    """Show the proper usage."""
    return "Try api-address:8000/predict/image_name"


@app.get("/predict/{image_name}")
def predict(image_name: str) -> int:
    """Predict the digit input image."""
    print(f"received {image_name}")
    return predict_digit.delay(image_name).get()


@app.get("/predict/triton/{image_name}")
def predict_triton(image_name: str) -> int:
    """Predict the digit input image w/ Triton Server."""
    print(f"received {image_name}")
    return predict_digit_triton.delay(image_name).get()
