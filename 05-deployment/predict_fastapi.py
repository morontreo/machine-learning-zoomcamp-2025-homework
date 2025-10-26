import pickle

from typing import Dict, Any

import uvicorn
from fastapi import FastAPI


app = FastAPI(title="ping")

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

@app.post("/predict")
def predict(client: Dict[str, Any]):
    result = pipeline.predict_proba(client)[0,1]
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)