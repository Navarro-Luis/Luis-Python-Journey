from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('./index.html')

@app.route("/blog")
def blog():
    return "these are my thoughts on blogs"

@app.route("blog/2020/dogs")
def blog2():
    return "this is my dog"
