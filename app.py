#coding: utf-8

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/status')
def status():
    return render_template('status.html')
    #Return 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
