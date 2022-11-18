import json
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return  render_template ("index.html")


@app.route("/load")
def loading():
    return  render_template ("loading_indicator.html")


if __name__ == "__main__":
    app.run(debug=True)