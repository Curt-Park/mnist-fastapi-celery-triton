# -*- coding: utf-8 -*-
"""Pretictors for handwritten digits recognition."""

import os
from typing import Tuple

import torch
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException

MODEL_PATH = os.path.join("model_repository", "mnist_cnn", "1", "model.pt")
TRITON_SERVER_URL = os.environ.get("TRITON_URL", "localhost:9000")


class BasePredictor:
    """Super class."""

    def predict(self, _: torch.FloatTensor) -> int:
        """Predict the digit."""
        raise NotImplementedError


class Predictor(BasePredictor):
    """Predictor that has a CNN model."""

    def __init__(self, model_path: str = MODEL_PATH) -> None:
        """Initialize."""
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.jit.load(model_path, map_location=self.device)
        self.model.eval()
        self.model_path = model_path

    def predict(self, image: torch.FloatTensor) -> int:
        """Predict a handwritten digit."""
        logits = self.model(image.to(self.device))
        prediction = torch.argmax(logits).detach().cpu().item()
        return int(prediction)


class PredictorTriton(BasePredictor):
    """Predictor that has a CNN model."""

    def __init__(
        self,
        model_name: str = "mnist_cnn",
        input_name: str = "input__0",
        output_name: str = "output__0",
        input_shape: Tuple[int, ...] = (1, 1, 28, 28),
    ) -> None:
        """Initialize."""
        self.url = TRITON_SERVER_URL
        self.model_name = model_name
        self.client = httpclient.InferenceServerClient(url=self.url, verbose=False)
        self.inputs = [httpclient.InferInput(input_name, input_shape, "FP32")]
        self.outputs = [httpclient.InferRequestedOutput(output_name, binary_data=False)]
        self.output_name = output_name

    def predict(self, image: torch.FloatTensor) -> int:
        """Predict a handwritten digit."""
        try:
            self.inputs[0].set_data_from_numpy(image.numpy(), binary_data=False)
            results = self.client.infer(
                self.model_name, self.inputs, outputs=self.outputs
            )
            _ = results.get_response()  # wait for the response
            output = results.as_numpy(self.output_name)
            prediction = output.argmax()
        except InferenceServerException:
            return -1
        return int(prediction)
