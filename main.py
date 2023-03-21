from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    post_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=post_url)
    response.raise_for_status()
    post_data = response.json()
    return render_template("index.html", posts = post_data)


if __name__ == "__main__":
    app.run(debug=True, port=9000)
