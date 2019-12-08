from flask import Flask, render_template

app = Flask(__name__)

from app import sql_connection

@app.route("/delta")
def hello():
    return render_template('delta.html')

