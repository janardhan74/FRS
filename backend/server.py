from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Add CORS middleware to allow the React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this as per your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded file locally or process it as needed
        contents = await file.read()
        with open(f"uploaded_{file.filename}", "wb") as f:
            f.write(contents)

        return {"message": "Image uploaded successfully!"}
    except Exception as e:
        return {"error": str(e)}
