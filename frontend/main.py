import requests
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form["input"]
    url = 'http://be86-64-228-155-213.ngrok.io/query'
    myobj = {'query': text}
    x = requests.post(url, data=myobj)
    x = x.json()
    confidence = str(round(float(x["confidence"]), 4))
    if x["prediction"] == "real":
        return render_template("real.html", confidence=confidence)
    else:
        return render_template("fake.html", confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
