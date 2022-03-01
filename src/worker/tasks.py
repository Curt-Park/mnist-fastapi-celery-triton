# -*- coding: utf-8 -*-
"""Producer."""
from .celery import app


@app.task
def predict_digit(image_name: str) -> int:
    """Predict a handwritten digit image."""
    print(f"received {image_name}")
    return 0


@app.task
def predict_digit_triton(image_name: str) -> int:
    """Predict a handwritten digit image with Triton."""
    print(f"received {image_name}")
    return 0
