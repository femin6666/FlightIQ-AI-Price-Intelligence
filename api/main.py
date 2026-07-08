from fastapi import FastAPI
import joblib

app = FastAPI(title="FlightIQ API")

# Load trained model
model = joblib.load("models/flight_price_model.pkl")


@app.get("/")
def home():
    return {
        "message": "FlightIQ API is Running!"
    }