"""Backend for KHIT Student Portal.
Run:  pip install flask  ->  python app.py  ->  open http://localhost:5000
"""
import json, os
from flask import Flask, jsonify, redirect, request, send_from_directory

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "students.json")


def load():
    try:
        with open(DATA, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return []


@app.route("/")
def home():
    return send_from_directory(BASE, "student-portal.html")


@app.route("/contact")
def contact():
    return redirect("https://kallamsociety.org.in/")


@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(load())


@app.route("/api/students", methods=["PUT"])
def save_students():
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(request.get_json(force=True), f, indent=2)
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(debug=True)
