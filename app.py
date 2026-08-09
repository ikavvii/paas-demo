from flask import Flask
import os

application = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY", "Not defined")

@application.route("/")
def home():
    return """
    <html>
        <head>
            <title>PaaS Demo</title>
        </head>
        <body>
            <h1>Welcome to AWS Elastic Beanstalk!</h1>
            <p>This application is deployed using PaaS.</p>
            <p>Kavin's Secret: {SECRET_KEY}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    application.run()