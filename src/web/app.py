from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global değişkenler
scores = {"red": 0, "blue": 0}
timer = "2:00"

@app.route("/")
def audience_display():
    """Audience Display sayfasını döner."""
    return render_template("audience.html", scores=scores, timer=timer)

@app.route("/scorekeeper")
def scorekeeper():
    """Scorekeeper sayfasını döner."""
    return render_template("scorekeeper.html", scores=scores)

@app.route("/update_score", methods=["POST"])
def update_score():
    """Skorları günceller."""
    global scores
    data = request.get_json()
    team = data.get("team")
    points = data.get("points")

    if team in scores:
        scores[team] += points
        return jsonify({"success": True, "scores": scores}), 200
    return jsonify({"success": False, "message": "Invalid team"}), 400

if __name__ == "__main__":
    app.run(debug=True)
