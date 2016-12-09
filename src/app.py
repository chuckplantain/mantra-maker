from flask import Flask, jsonify, render_template, redirect, url_for
from mantra_maker import main

app = Flask(__name__)
app.config.from_object('config.Development')

@app.route('/mantra')
def mantra_maker():
    return jsonify(result=main())

@app.route('/')
def index():
    return redirect(url_for('mantra_maker'), code=302)

@app.route('/posting')
def handler():
    pass

if __name__ == "__main__":
    app.run()
