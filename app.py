from flask import Flask
from flask import render_template

app = Flask (__name__)

@app.route('/')
@app.route('/index.html/')
def main_page():
    return render_template('index.html')
