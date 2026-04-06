import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data.csv")

X = data[["size_kb", "requests", "load_time"]]
y = data["carbon"]

model = LinearRegression()
model.fit(X, y)

def predict(size_kb, requests, load_time):
    return model.predict([[size_kb, requests, load_time]])[0]