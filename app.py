from flask import Flask, render_template, jsonify
from gold_rate_checker.checker import parse_gold_rate, should_alert
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    try:
        rate = parse_gold_rate()
        alert = should_alert(rate)
    except Exception as e:
        rate = "Error"
        alert = False
        print(f"Error fetching rate: {e}")

    return render_template("index.html", rate=rate, alert=alert, time=datetime.datetime.now())

@app.route("/api/gold-rate")
def api_gold_rate():
    try:
        rate = parse_gold_rate()
        alert = should_alert(rate)
        return jsonify({
            "rate": rate,
            "alert": alert,
            "timestamp": datetime.datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
