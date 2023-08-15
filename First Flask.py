from time import sleep
from flask import Flask, redirect, url_for
import pyautogui as pg
import webbrowser as wb

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"
wb.open("http://127.0.0.1:5000")

@app.route("/<name>")
def user(name):
    return f"Hello! You are in the page of {name}!"
print("Done!")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run()