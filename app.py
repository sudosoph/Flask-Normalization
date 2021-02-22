from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if  __name__ == "__maine__":
    app.run()

