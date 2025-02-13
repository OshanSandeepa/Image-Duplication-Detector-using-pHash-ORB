
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import mysql.connector
import cv2
import numpy as np
import imagehash
from PIL import Image
import io

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://localhost:5174"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)



# Connect to MySQL
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "image_db"
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Compute pHash
def compute_phash(image: Image.Image):
    return str(imagehash.phash(image))

# ORB Feature Matching
def compute_orb_similarity(img1, img2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return 0  # No features found

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    return len(matches) / max(len(kp1), len(kp2))  # Similarity score

@app.post("/compare/")
async def compare_images(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    # Read image bytes
    img1_bytes = await file1.read()
    img2_bytes = await file2.read()

    img1 = Image.open(io.BytesIO(img1_bytes))
    img2 = Image.open(io.BytesIO(img2_bytes))

    # Compute pHash
    hash1 = compute_phash(img1)
    hash2 = compute_phash(img2)

    # pHash similarity check
    hash_similarity = 1 - (imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)) / len(hash1)

    # Convert images to grayscale for ORB
    img1_np = cv2.imdecode(np.frombuffer(img1_bytes, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    img2_np = cv2.imdecode(np.frombuffer(img2_bytes, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

    # ORB feature similarity check
    orb_similarity = compute_orb_similarity(img1_np, img2_np)

    return {
        "pHash_similarity": hash_similarity,
        "ORB_similarity": orb_similarity
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
