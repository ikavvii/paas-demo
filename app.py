from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This application is running on PaaS."

if __name__ == "__main__":
    app.run()
