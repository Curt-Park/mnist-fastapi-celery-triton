# -*- coding: utf-8 -*-
"""Locus file for load tests.

- Author: Jinwoo Park
- Email: www.jwpark.co.kr@gmail.com

Reference:
    http://docs.locust.io/en/stable/writing-a-locustfile.html
    http://docs.locust.io/en/stable/increase-performance.html
    http://docs.locust.io/en/stable/running-distributed.html
"""
from typing import Any

from locust import FastHttpUser, task


class MnistPredictionUser(FastHttpUser):
    """Send auto-polygon requests."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize."""
        super().__init__(*args, **kwargs)
        self.service = "/predict/mnist_sample.jpg"

    @task
    def predict_digits(self) -> None:
        """Request auto-polygon with any cropped image."""
        # send
        self.client.get(self.service)


class MnistPredictionTritonUser(MnistPredictionUser):
    """Send auto-polygon requests."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize."""
        super().__init__(*args, **kwargs)
        self.service = "/predict/triton/mnist_sample.jpg"
