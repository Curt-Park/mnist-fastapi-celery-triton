# -*- coding: utf-8 -*-
"""Pretictors for handwritten digits recognition."""

import os
from typing import Tuple

import numpy as np
import torch
import tritonclient.http as httpclient
import tritonclient.utils.shared_memory as shm
from tritonclient import utils

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
        input_info: Tuple[str, Tuple[int, ...]] = ("input__0", (1, 1, 28, 28)),
        output_info: Tuple[str, Tuple[int, ...]] = ("output__0", (1, 10)),
        type_name: str = "FP32",
    ) -> None:
        """Initialize."""
        url = TRITON_SERVER_URL
        self.model_name = model_name
        self.output_name, output_shape = output_info
        self.input_name, input_shape = input_info

        self.client = httpclient.InferenceServerClient(url=url, verbose=False)
        self.__init_shared_memory(input_shape, output_shape, type_name)

    def __init_shared_memory(
        self,
        input_shape: Tuple[int, ...],
        output_shape: Tuple[int, ...],
        type_name: str,
    ) -> None:
        """Initialize shared memory for speed up."""
        # to make sure no shared memory regions are registered with the server.
        self.client.unregister_system_shared_memory()
        self.client.unregister_cuda_shared_memory()

        # get input / output information
        input_data = np.zeros(input_shape, dtype=np.float32)
        output_data = np.zeros(output_shape, dtype=np.float32)
        intput_byte_size = input_data.size * input_data.itemsize
        output_byte_size = output_data.size * output_data.itemsize

        # register shared memory for inputs and outputs
        self.shm_op_handle = shm.create_shared_memory_region(
            "output_data", f"/output_{self.model_name}", output_byte_size
        )
        self.client.register_system_shared_memory(
            "output_data", f"/output_{self.model_name}", output_byte_size
        )
        shm_ip_handle = shm.create_shared_memory_region(
            "input_data", f"/input_{self.model_name}", intput_byte_size
        )
        shm.set_shared_memory_region(shm_ip_handle, [input_data])
        self.client.register_system_shared_memory(
            "input_data", f"/input_{self.model_name}", intput_byte_size
        )

        # set parameters to use data from shared memory
        self.inputs = [httpclient.InferInput(self.input_name, input_shape, type_name)]
        self.inputs[-1].set_shared_memory("input_data", intput_byte_size)
        self.outputs = [
            httpclient.InferRequestedOutput(self.output_name, binary_data=True)
        ]
        self.outputs[-1].set_shared_memory("output_data", output_byte_size)

    def predict(self, image: torch.FloatTensor) -> int:
        """Predict a handwritten digit."""
        self.inputs[-1].set_data_from_numpy(image.numpy().astype(np.float32))
        results = self.client.infer(self.model_name, self.inputs, outputs=self.outputs)
        output = results.get_output(self.output_name)
        if output is None:
            return -1

        output = shm.get_contents_as_numpy(
            self.shm_op_handle,
            utils.triton_to_np_dtype(output["datatype"]),
            output["shape"],
        )
        prediction = output.argmax()
        return int(prediction)
