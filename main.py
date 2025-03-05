# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
model = joblib.load("iris_model.pkl")

app = FastAPI()


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(iris: IrisInput):
    data = np.array(
        [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
    )
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
