import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form["input"]
    url = 'http://bb74-34-82-224-201.ngrok.io/query'
    myobj = {'query': text}
    x = requests.post(url, data=myobj)
    x = x.json()
    confidence = round(float(x["confidence"]), 4)
    if x["prediction"] == "real":
        return render_template("real.html", confidence=abs(100-int(confidence)))
    else:
        return render_template("fake.html", confidence=abs(int(confidence)))

if __name__ == "__main__":
    app.run(debug=True)