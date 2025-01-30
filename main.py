from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this later)
    allow_methods=["GET"],  # Restrict HTTP methods
    allow_headers=["*"],
)

# Sample product data
products = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

# Define the `/products` route
@app.get("/products")
async def get_products():
    return products

# Run with: `uvicorn main:app --host 0.0.0.0 --port 3030`

