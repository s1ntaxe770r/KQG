from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://api.kanye.rest"
    data = requests.get(url)
    response = data.json()
    quote = response["quote"]

    return render_template("index.html",quote=quote)   


if __name__ == "__main__":
    app.run(host="0.0.0.0")