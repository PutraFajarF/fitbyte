from fastapi import APIRouter
from app.api.v1.endpoints import profile

api_router = APIRouter()
api_router.include_router(profile.router, prefix="", tags=["user"])