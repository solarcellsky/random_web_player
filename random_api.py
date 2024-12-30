import sys
import os
from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import random


app = FastAPI()

# 跨域处理
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

def read_random_line(file_path: str) -> str:
    """Reads a random line from a given file."""
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        raise HTTPException(status_code=400, detail="File is empty")

    return random.choice(lines).strip()


@app.get("/")
async def get_random_video_url():
    """Returns a random video URL from the video.txt file."""
    try:
        file_path = "./video_urls.txt"
        random_line = read_random_line(file_path)
        # Assuming each line contains only one URL
        return {"url": random_line}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))