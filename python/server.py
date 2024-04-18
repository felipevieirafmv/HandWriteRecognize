from flask import Flask, render_template, request
from realPictures import prediction
from tensorflow.keras import models

app = Flask(__name__)

model = models.load_model("checkpoints/87-83.keras")

@app.route('/')
def predict():
    result = prediction(model)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000)