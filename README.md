# Quranic Search API

## 📌 Overview
Quranic Search API is a FastAPI-based service that allows users to search for Quranic verses using **MongoDB**, **Cohere embeddings**, and **Qdrant vector search** for accurate and efficient retrieval.

## 🚀 Features
- **Search Quranic verses** using text-based queries.
- **Vector similarity search** for enhanced results.
- **Dependency injection** for modular and scalable architecture.
- **Optimized MongoDB queries** for fast response times.

## 🏗️ Project Structure
app/ │── api/ # API endpoints (search router) │── core/ # Core configuration and utilities │── models/ # Data models and schemas │── services/ # Business logic (SearchService) │── dependencies.py # Dependency injection setup │── main.py # Application entry point ├── tests/ # Unit tests ├── requirements.txt # Dependencies ├── README.md # Project documentation


## 📦 Installation
### 1️⃣ Clone the Repository

```
git clone [https://github.com/your-username/quranic-search-api.git](https://github.com/zifo-10/Qurani-AI.git)
```

2️⃣ Create a Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
🛠️ Configuration
Environment Variables
Create a .env file and add the following variables:
```
MONGO_URI=mongodb://localhost:27017
QDRANT_HOST=http://localhost:6333
COHERE_API_KEY=your-cohere-api-key
```
▶️ Running the API
Start FastAPI Server
```
uvicorn app.main:app --reload
```

Test the Search Endpoint
```
curl -X 'GET' "http://127.0.0.1:8000/search?query=your-text" -H "accept: application/json"
🧪 Running Tests
```





