from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def portfoli():
    return render_template('portfoli.html')  

if __name__ == '__main__':
    app.run(debug=True)
