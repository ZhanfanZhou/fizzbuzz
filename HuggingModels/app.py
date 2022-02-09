import json
import requests
from flask import Flask

APP_NAME = "Hugging Models"
API_TOKEN = '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'
API_URL_PRE = f"https://api-inference.huggingface.co/models/"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def ez_query(model_id, payload):
    API_URL = API_URL_PRE + model_id
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


app = Flask(APP_NAME)


@app.route("/")
def hello():
    return f"Hello, {APP_NAME}!"


@app.route('/models/<model_id>/<query>', methods=['POST', 'get'])
# Get data from json and return the requested row defined by the variable Line
def models(model_id, query):
    query = query.replace("-", ' ')
    return ez_query(model_id, query)[0]


app.run(debug=True, host='0.0.0.0', port=5001)
