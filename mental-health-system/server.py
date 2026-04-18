from flask import Flask, request, jsonify, render_template, url_for, redirect
from algorithm import calculate_mood
from questionnaires import depression, anxiety, adhd, ptsd, bipolar

# Decided to try the Jinja2 template since it passes data from Flask to HTML
# Here's a video to look into it: https://www.youtube.com/watch?v=eghZ5Q0GPhs

app = Flask(__name__)

TEST_URL = {
    "depression": depression,
    "anxiety": anxiety,
    "adhd": adhd,
    "ptsd": ptsd,
    "bipolar": bipolar
}

@app.route("/")
def home():
    return render_template("home.html", tests=TEST_URL.keys())

@app.route("/questionnaires/<test_id>")
def test_page(test_id):
    module = TEST_URL.get(test_id)
    if not module:
        return redirect(url_for("home"))

    questions_list, scale,prompt = module.questions()

    return render_template("check_in.html", questions=questions_list, scale=scale, prompt=prompt, test_id=test_id)

@app.route("/checkin", methods=["POST"])
def checkin():

    if request.form:
        test_id = request.form.get("test_id")
        totals = {"stressed": 0, "happy": 0, "motivation": 0}

        for key, value in request.form.items():
            for relevant_mood in totals.keys():
                if key.startswith(relevant_mood):
                    totals[relevant_mood] += int(value)

        mood = calculate_mood(totals["stressed"], totals["happy"], totals["motivation"], test_id)
        return render_template("results.html", mood=mood)

    else:
        data = request.json

        mood = calculate_mood(
            data["stressed"],
            data["happy"],
            data["motivation"],
            data["test_id"]
        )

        return jsonify({"mood":mood})

if __name__ == "__main__":
    app.run(port=5000, debug=True)