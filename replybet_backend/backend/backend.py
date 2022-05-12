from fastapi import FastAPI, APIRouter
from routes.users import router as UsersRouter


backend = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

backend.include_router(UsersRouter, tags = ["Users"], prefix = "/users")