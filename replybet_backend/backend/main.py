from fastapi import FastAPI, APIRouter
import logging


import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend:backend", host="0.0.0.0", port=8001, log_level="debug")