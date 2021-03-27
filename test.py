import json
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/welcome/', methods=['GET'])
def welcome():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    return json.loads(response.text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
