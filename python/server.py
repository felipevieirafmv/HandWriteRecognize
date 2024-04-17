from flask import Flask, render_template, request
from realPictures import prediction

app = Flask(__name__)

@app.route('/')
def predict():
    result = prediction()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000)