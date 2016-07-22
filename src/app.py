from mantra_maker import main
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
FlaskJSON(app)

@app.route('/')
def hello_world():
    return json_response(result=main())

if __name__ == "__main__":
    app.run()
