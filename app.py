from flask import Flask, render_template, request
import os
from document_processor import extract_text
from risk_model import calculate_risk
from cam_generator import generate_cam

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files.get("document")

    if not file:
        return "No document uploaded"

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    text = extract_text(path)

    risk_score, risk_level = calculate_risk(text)

    cam = generate_cam(risk_score, risk_level)

    return render_template(
        "result.html",
        score=risk_score,
        level=risk_level,
        cam=cam
    )


if __name__ == "__main__":
    app.run(debug=True)
