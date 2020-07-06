import os
import io
import time
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
app = Flask(__name__)

# <--プログラム-->

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/test')
def index2():
    return 'Hello test!'

@app.route("/index") #アプリケーション/indexにアクセスが合った場合
def index():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))