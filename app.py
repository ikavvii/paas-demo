from flask import Flask
import os

app = Flask(__name__)

secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    return f"Hello! This application is running on PaaS. Kavin's secret: {SECRET_KEY}"

if __name__ == "__main__":
    app.run()
