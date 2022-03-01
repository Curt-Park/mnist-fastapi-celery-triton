# -*- coding: utf-8 -*-
"""Celery configurations."""
import os

from celery import Celery

broker = os.environ.get("BROKER_URL", "redis://localhost:6379")
backend = os.environ.get("BACKEND_URL", "redis://localhost:6379")
triton = os.environ.get("TRITON_URL", "localhost:9000")


app = Celery(
    __name__,
    broker=broker,
    backend=backend,
    include=["worker.tasks"],
)


app.conf.update(result_expires=3600)
