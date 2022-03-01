# -*- coding: utf-8 -*-
"""API server that accepts requests and returns values."""
from fastapi import FastAPI
from pydantic import BaseModel

from worker.tasks import produce


class TaskResult(BaseModel):
    """Return value."""

    value: int


app = FastAPI()


@app.get("/ping")
def ping() -> str:
    """Ping."""
    return "pong"


@app.get("/produce")
def produce_value() -> TaskResult:
    """Produce an integer value."""
    result = produce.delay()
    value = result.get()  # await until done
    return TaskResult(value=value)
