from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    names=['小可愛','長頸鹿']
    return render_template("index.jinja.html",names=names)
@app.route("/kiki")
def kiki():
    return render_template("kiki.jinja.html")
@app.route("/lulu")
def lulu():
    return render_template("lulu.jinja.html")
@app.route("/dayday")
def dayday():
    return render_template("dayday.jinja.html")