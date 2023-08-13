from flask import Flask
import pyautogui as pg
import webbrowser as wb

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()
    wb.open("http://127.0.0.1:5000")
    pg.moveTo(700, 800, duration=10)