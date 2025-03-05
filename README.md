# Iris Prediction API

This project is a machine learning API that predicts the species of Iris flowers based on their measurements.

## Installation

To install the required packages, run:

```bash
pip install -r requirements.txt
```

## How to Train the Model

To train the model, run:

```bash
python train_model.py
```

This will create a file named `iris_model.pkl` in the project directory.

## How to Run the API

To run the FastAPI application, execute:

```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

You can then access the API at `http://localhost/predict`.

## Using Docker

To run the application in a Docker container, build the image and run it:

```bash
docker build -t iris-prediction-api .
docker run -p 80:80 iris-prediction-api
```

## Example API Request

To make a prediction, send a POST request to `/predict` with the following JSON body:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

The response will contain the predicted species.
