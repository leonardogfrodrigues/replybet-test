from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.registers import Users, Clients
from requester import ErrorReturn, request
from backend import backend

import json
import logging

log = logging.getLogger()
router = APIRouter()

api_router = APIRouter()

# 3
@api_router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "Hello, World!"}

backend.include_router(api_router)