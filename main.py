from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from datetime import datetime
from typing import List
from fastapi.responses import HTMLResponse
from fastapi import Header, HTTPException
import base64

app = FastAPI()

# Liste en mémoire pour stocker les posts
posts = []

# Modèle de données pour les posts
class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

# Q1: Route GET /ping
@app.get("/ping", response_class=HTMLResponse)
async def ping():
    return "pong"
