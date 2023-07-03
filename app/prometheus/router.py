import time
from random import random

from fastapi import APIRouter

router = APIRouter(prefix="/prometheus", tags=["Testing Grafana + Prometheus"])


@router.get("/get_error")
def get_error():
    if random() > 0.5:
        raise ZeroDivisionError
    else:
        raise KeyError


@router.get("/time_consumer")
def time_consumer():
    time.sleep(random() * 5)
    return 1


@router.get("/memory_consumer")
def memory_consumer():
    _ = [i for i in range(30_000_000)]
    return 1
