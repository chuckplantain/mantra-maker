from main import main
from flask import Flask
app = Flask(__name__)

@app.route('/mantra/')
def hello_world():
    return main()


if __name__ == "__main__":
    app.run()
