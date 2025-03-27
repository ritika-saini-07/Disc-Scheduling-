import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

class AIScheduler:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)
        joblib.dump(self.model, "models/trained_model.pkl")

    def predict(self, requests):
        model = joblib.load("models/trained_model.pkl")
        return sorted(requests, key=lambda x: model.predict(np.array([[x]]))[0])

ai_scheduler = AIScheduler()
