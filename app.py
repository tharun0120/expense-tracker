from flask import Flask, render_template, redirect, session
from flask_session import Session

from routes.users import userBp

from dotenv import load_dotenv

import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

app.register_blueprint(userBp)


@app.route("/")
def index():
    if session.get("active") == None:
        return render_template("index.html")
    else:
        return redirect("/dash")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.run("127.0.0.1", 8000, debug=True)
