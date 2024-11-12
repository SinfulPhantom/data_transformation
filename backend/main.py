from pathlib import Path

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

UPLOAD_DIR = Path() / 'uploads'

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World!"}

@app.post("/uploadfile/")
async def upload_file(file_uploads: list[UploadFile]) -> dict:
    for file_upload in file_uploads:
        data = await file_upload.read()
        save_to = UPLOAD_DIR / file_upload.filename
        with open(save_to, 'wb') as f:
            f.write(data)
    return {"filenames": [f.filename for f in file_uploads]}