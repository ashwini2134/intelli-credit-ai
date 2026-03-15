from flask import Flask, render_template, request, send_file
import os
import sqlite3

from document_processor import extract_text
from risk_model import calculate_risk
from cam_generator import generate_cam
from financial_analyzer import extract_financials

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -------------------------------
# DATABASE FUNCTION
# -------------------------------

def save_analysis(company, score, level):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            company TEXT,
            score INTEGER,
            level TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO history VALUES (?, ?, ?)",
        (company, score, level)
    )

    conn.commit()
    conn.close()


# -------------------------------
# ROUTES
# -------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------------------
# ANALYZE DOCUMENT
# -------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["document"]

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    # Extract text from document
    text = extract_text(path)

    # Extract financial data
    financials = extract_financials(text)

    # Calculate risk
    score, level = calculate_risk(text, financials)

    borrower = "Tata"

    research = "Risk Level: MEDIUM. Some legal and financial developments found in web search."

    # Generate CAM report
    cam_file = generate_cam(score, level, borrower, financials, research)

    # Save history
    save_analysis(borrower, score, level)

    return render_template(
        "result.html",
        score=score,
        level=level,
        financials=financials,
        cam_file=cam_file
    )


# -------------------------------
# DOWNLOAD CAM
# -------------------------------

@app.route("/download_cam")
def download_cam():

    financials = {
        "Revenue": "₹1,80,00,000",
        "Profit": "₹32,00,000",
        "Total Debt": "₹90,00,000",
        "Total Assets": "₹2,10,00,000"
    }

    research = "Risk Level: MEDIUM. Several legal cases and financial developments were identified."

    file = generate_cam(90, "MEDIUM", "Tata", financials, research)

    return send_file(file, as_attachment=True)


# -------------------------------
# HISTORY PAGE
# -------------------------------

@app.route("/history")
def history():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history")

    rows = cursor.fetchall()

    history_data = []

    for r in rows:
        history_data.append({
            "company": r[0],
            "score": r[1],
            "level": r[2]
        })

    conn.close()

    return render_template("history.html", history=history_data)


# -------------------------------
# RUN APP
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)
