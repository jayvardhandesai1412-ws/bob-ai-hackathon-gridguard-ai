from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/risk")
def risk():
    return jsonify({
        "transformer": "T-101",
        "risk_score": 82,
        "status": "High Risk",
        "reason": "High temperature + rain forecast"
    })

if __name__ == "__main__":
    app.run(debug=True)
