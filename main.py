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

# Q2: Route GET /home
@app.get("/home", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <body>
            <h1>Welcome home!</h1>
        </body>
    </html>
    """

# Q3: Gestion des routes inconnues
@app.get("/404", response_class=HTMLResponse)
async def not_found():
    return """
    <html>
        <body>
            <h1>404 NOT FOUND</h1>
        </body>
    </html>
    """


#Q4
@app.get("/ping")
async def ping():
    return "pong"


# Q5: Route GET /post
@app.get("/posts", response_model=List[Post])
async def get_posts():
    return posts

# Q6: Route PUT /post
@app.put("/posts")
async def update_post(post: Post):
    for index, existing_post in enumerate(posts):
        if existing_post.title == post.title:
            posts[index] = post
            return post
    posts.append(post)
    return post

# Q7: BONUS
def verify_credentials(authorization: str = Header(...)):
    credentials = authorization.split(" ")[1]
    decoded_credentials = base64.b64decode(credentials).decode("utf-8")
    username, password = decoded_credentials.split(":")
    if username == "admin" and password == "123456":
        return True
    raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/ping/auth", response_class=HTMLResponse)
async def ping_auth(authorized: bool = Depends(verify_credentials)):
    return "pong"
