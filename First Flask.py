import random
from time import sleep
from flask import Flask, redirect, url_for, render_template, request
import pyautogui as pg
import webbrowser as wb

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
@app.route("/<name>/")
@app.route("/<name>/<surname>")
def user(name, surname=""):#document.querySelector("#para")//*[@id="para"]/html/body/div/p[3]/html/body/div/p[2]
    return render_template("user.html", content=F"{name} & {surname}")

print("Done!")
@app.route("/search", methods=['GET'])
def search():
    args = request.args
    return str(args.to_dict()) + str(args.get("query"))

@app.route(f"/Damn it's him/{random.random()}")
def specialUser():
    return render_template("user.html", content="Holy Admin!")
    
@app.route("/admin/")
def admin():
    return redirect(url_for("specialUser"))

@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    # wb.open("http://127.0.0.1:5000")
    app.run(debug=True)