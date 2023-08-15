from time import sleep
from flask import Flask, redirect, url_for, render_template
import pyautogui as pg
import webbrowser as wb

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/<name>")
# def user(name, k):
#     return render_template("user.html", content=name)
print("Done!")

@app.route("/Damn it's him/hrthjtr")
def specialUser():
    return render_template("user.html", content="Holy Admin!")
    
@app.route("/admin")
def admin():
    return redirect(url_for("specialUser"))

if __name__ == "__main__":
    # wb.open("http://127.0.0.1:5000")
    app.run(debug=True)