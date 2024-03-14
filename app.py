from flask import Flask, send_from_directory, render_template, request, redirect
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    file_list = os.listdir("static")
    return render_template("index.html", file_list=file_list)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
