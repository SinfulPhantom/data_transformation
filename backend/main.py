import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World!"}

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)) -> dict:
    data = await file.read()
    save_to = f"./{file.filename}"
    with open(save_to, 'wb') as f:
        f.write(data)
    return {"filename": file.filename}