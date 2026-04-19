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
DISPLAY_NAMES = {
    "depression": "Depression",
    "anxiety": "Anxiety",
    "adhd": "ADHD",
    "ptsd": "PTSD",
    "bipolar": "Bipolar Disorder"
}
@app.route("/")
def home():
    return render_template("home.html", tests=TEST_URL.keys(), display_names=DISPLAY_NAMES)

@app.route("/questionnaires/<test_id>")
def test_page(test_id):
    module = TEST_URL.get(test_id)
    if not module:
        return redirect(url_for("home"))

    questions_list, scale,prompt = module.questions()
    scale_max = {"depression": 3, "anxiety": 3, "adhd": 4, "ptsd": 4, "bipolar": 1}
    max_val= scale_max.get(test_id, 4)
    return render_template("check_in.html", questions=questions_list, scale=scale, prompt=prompt, test_id=test_id, max_val=max_val, display_names=DISPLAY_NAMES)

@app.route("/checkin", methods=["POST"])
def checkin():

    if request.form:
        test_id = request.form.get("test_id")
        totals = {"stressed": 0, "happy": 0, "motivation": 0}

        scale_max= {"depression": 3, "anxiety": 3, "adhd": 4, "ptsd": 4, "bipolar": 1}
        max_val = scale_max.get(test_id, 4)
        for key, value in request.form.items():
            for relevant_mood in totals.keys():
                if key.startswith(relevant_mood):
                    answer = int(value)
                    if answer < 0 or answer > max_val:
                        return render_template("check_in.html", questions=TEST_URL[test_id].questions()[0], scale=TEST_URL[test_id].questions()[1], prompt=TEST_URL[test_id].questions()[2], test_id=test_id, max_val=max_val, display_names=DISPLAY_NAMES, error="Invalid input: values must be between 0 and {}".format(max_val))
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