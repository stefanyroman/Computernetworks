from flask import Flask, request, jsonify
from algorithm import calculate_mood

app = Flask(__name__)

@app.route("/checkin", methods=["POST"])
def checkin():

    data = request.json

    mood = calculate_mood(
        data["stressed"],
        data["happy"],
        data["motivation"]
    )

    return jsonify({"mood":mood})

if __name__ == "__main__":
    app.run(port=5000, debug=True)