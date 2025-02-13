# Image Duplication Detector

## Overview
This project is an **image duplication detection system** that uses **pHash (Perceptual Hashing) and ORB (Oriented FAST and Rotated BRIEF)** to analyze image similarities. The system allows users to upload images, which are then processed using advanced image hashing and feature detection techniques to determine duplication.

## Features
✅ **Image Comparison using pHash & ORB**  
✅ **Similarity Scoring System**  
✅ **MySQL Database Integration** for storing image hashes  
✅ **FastAPI Backend** for image processing  
✅ **REST API for Uploading & Checking Images**  
✅ **Docker Support** for containerized deployment  
✅ **CI/CD Integration with GitHub Actions**  

## Tech Stack
- **Backend:** FastAPI, Uvicorn, OpenCV, NumPy
- **Database:** MySQL
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions

## Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/image-duplication-detector.git
cd image-duplication-detector
```

### 2️⃣ Set Up Virtual Environment & Install Dependencies
```sh
cd backend
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows
pip install -r requirements.txt
```

### 3️⃣ Run Backend Server
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ Set Up Database
Create a MySQL database:
```sql
CREATE DATABASE image_db;
```
Update database credentials in `.env` file.

### 5️⃣ Run with Docker
```sh
docker-compose up --build -d
```

## API Endpoints
### 🔹 Upload an Image
```http
POST /upload
```
### 🔹 Check for Duplicate Images
```http
POST /check-duplicate
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

