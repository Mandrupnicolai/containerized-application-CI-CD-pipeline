from __future__ import annotations

import os

from fastapi import FastAPI

APP_NAME = os.getenv("APP_NAME", "containerized-app")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/")
def root() -> dict[str, str]:
    return {"name": APP_NAME, "version": APP_VERSION}


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}

