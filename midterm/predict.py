import pickle
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, Field

class WaterMetrics(BaseModel):
    ph: float
    hardness: float
    solids: float
    chloramines: float
    sulfate: float
    conductivity: float
    organic_carbon: float
    trihalomethanes: float
    turbidity: float

class PredictResponse(BaseModel):
    potability_probability: float
    potability: bool

app = FastAPI(title="water-potability-prediction")

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(waterMetrics):
    result = pipeline.predict_proba(waterMetrics)[0, 1]
    return float(result)

@app.post("/predict")
def predict(waterMetrics: WaterMetrics) -> PredictResponse:
    prob = predict_single(waterMetrics.model_dump())

    return PredictResponse(
        potability_probability=prob,
        potability=prob >= 0.60
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)