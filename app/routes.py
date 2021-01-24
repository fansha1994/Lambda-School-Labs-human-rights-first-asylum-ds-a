"""
Main routes for app
"""

from fastapi import FastAPI, APIRouter


router = APIRouter()

@router.get('hello')
async def hello():
    return 'Hello!'
