# -*- coding: utf-8 -*-
"""Producer."""
import time
from random import randint

from .celery import app


@app.task
def produce() -> int:
    """Produce a random value."""
    time.sleep(1)  # producing time
    return randint(1, 100)
