import json
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_var = [
    {"name": "alfa", "age": 20}, 
    {"name": "beta", "age": 21}, 
    {"name": "gama", "age": 15},
    ]


@app.route("/")
def home():
    return  render_template ("index.html")


@app.route("/load")
def loading():
    return  render_template ("loading_indicator.html")

@app.route("/data")
def data():
    return  data_var

    


if __name__ == "__main__":
    app.run(debug=True)