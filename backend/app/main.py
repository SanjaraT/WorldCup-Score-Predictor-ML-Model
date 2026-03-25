from fastapi import FastAPI
import pandas as pd
import pickle
from app.schema import MatchInput, PredictionResponse
import os
import requests

app = FastAPI(
    title="T20 Score Predictor API",
    description="Predicts final T20 cricket score based on current match situation",
    version="1.0"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "t20_score_predictor.pkl")

MODEL_URL = "https://huggingface.co/SanjuTuni/t20-score-predictor/resolve/main/t20_score_predictor.pkl"


def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")

        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

        response = requests.get(MODEL_URL)

        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)

        print("Model downloaded!")
        print("Model size:", os.path.getsize(MODEL_PATH))


def load_model():
    download_model()
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


model = load_model()

TOTAL_BALLS = 120
TOTAL_WICKETS = 10

def normalize_text(text: str) -> str:
    return text.strip().title()

@app.get("/")
def home():
    return {"message": "T20 Score Predictor API is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict_score(data: MatchInput):

   
    
    batting_team = normalize_text(data.batting_team)
    bowling_team = normalize_text(data.bowling_team)
    city = normalize_text(data.city)

    
    overs = float(data.overs)
    wickets = int(data.wickets)
    current_score = int(data.current_score)
    last_5_overs_runs = int(data.last_5_overs_runs)

   
    full_overs = int(overs)
    balls = round((overs - full_overs) * 10)

    if balls > 5:
        return PredictionResponse(
            predicted_score=0,
            message="Invalid input: balls in over cannot exceed 5"
        )

    balls_bowled = full_overs * 6 + balls
    balls_left = TOTAL_BALLS - balls_bowled

    # Data validations
    if overs < 0 or overs > 20:
        return PredictionResponse(predicted_score=0, message="Overs must be between 0 and 20")

    if wickets < 0 or wickets > 10:
        return PredictionResponse(predicted_score=0, message="Wickets must be between 0 and 10")

    wickets_left = TOTAL_WICKETS - data.wickets

    
    current_run_rate = (
        data.current_score / (balls_bowled / 6)
        if balls_bowled > 0 else 0
    )

    
    df = pd.DataFrame([{
        "batting_team": data.batting_team,
        "bowling_team": data.bowling_team,
        "city": data.city,
        "current_score": data.current_score,
        "balls_left": balls_left,
        "wickets_left": wickets_left,
        "current_run_rate": current_run_rate,
        "last_5_overs_runs": data.last_5_overs_runs
    }])

    prediction = model.predict(df)[0]

    return PredictionResponse(
        predicted_score=round(float(prediction), 2),
        message="Prediction successful"
    )