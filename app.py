from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/normalize")
def normalize():
    return 'Normalization script'

if  __name__ == "__main__":
    app.run()

