# -*- coding: utf-8 -*-
"""Pretictors for handwritten digits recognition."""

import os
from typing import Optional, Tuple

import torch
import tritonclient.http as httpclient

MODEL_PATH = os.path.join("model_repository", "mnist_cnn", "1", "model.pt")
TRITON_SERVER_URL = os.environ.get("TRITON_URL", "localhost:9000")


class Predictor:
    """Predictor that has a CNN model."""

    def __init__(self, model_path: str = MODEL_PATH) -> None:
        """Initialize."""
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_path = model_path
        self.model: Optional[torch.nn.Module] = None

    def _init_model(self) -> torch.nn.Module:
        """Load torch script model."""
        model = torch.jit.load(self.model_path, map_location=self.device)
        model.eval()
        return model

    def predict(self, image: torch.FloatTensor) -> int:
        """Predict a handwritten digit."""
        # lazy init for sementation annotator
        # celery doesn't support spawn, but pytorch only supports spawn
        # https://github.com/celery/celery/issues/6036
        if self.model is None:
            self.model = self._init_model()
        logits = self.model(image)
        prediction = torch.argmax(logits).detach().cpu().item()
        return int(prediction)


class PredictorTriton:
    """Predictor that has a CNN model."""

    def __init__(
        self,
        model_name: str = "mnist_cnn",
        input_shape: Tuple[int, ...] = (1, 1, 28, 28),
        input_type: str = "FP32",
    ) -> None:
        """Initialize."""
        self.url = TRITON_SERVER_URL
        self.model_name = model_name
        self.client = httpclient.InferenceServerClient(url=self.url, verbose=True)
        self.inputs = [httpclient.InferInput("input__0", input_shape, input_type)]
        self.outputs = [httpclient.InferRequestedOutput("output__0", binary_data=False)]

    def predict(self, image: torch.FloatTensor) -> int:
        """Predict a handwritten digit."""
        self.inputs[0].set_data_from_numpy(image.numpy(), binary_data=False)
        results = self.client.infer(self.model_name, self.inputs, outputs=self.outputs)
        logits = results.get_response().as_numpy("output__0")
        prediction = logits.argmax()
        return int(prediction)
