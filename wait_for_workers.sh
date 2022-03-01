#!/bin/sh
until PYTHONPATH=src celery -A src.worker.celery inspect ping; do
    echo "Celery workers not available"
    sleep 1
done
