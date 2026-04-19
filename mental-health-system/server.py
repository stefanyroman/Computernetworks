#import from storage
from storage import init_db, save_checkin, get_checkins_by_user

#import flask tools
from flask import Flask, request, jsonify, render_template, url_for, redirect, session
from functools import wraps

#import calculated results
from algorithm import calculate_mood

#import questionnaires
from questionnaires import depression, anxiety, adhd, ptsd, bipolar


#creates the Flask app
app = Flask(__name__)

#stores login state in the session
app.secret_key = "synapsenet-demo-secret-key"

#initialize database
init_db()


#connects each test name to correct questionnaire file
TEST_URL = {
    "depression": depression,
    "anxiety": anxiety,
    "adhd": adhd,
    "ptsd": ptsd,
    "bipolar": bipolar
}

#correct name display for each test
DISPLAY_NAMES = {
    "depression": "Depression",
    "anxiety": "Anxiety",
    "adhd": "ADHD",
    "ptsd": "PTSD",
    "bipolar": "Bipolar Disorder"
}

#user credentials for authentication
USERS = {
    "admin": "synapse123",
    "demo": "demo123"
}


#protects routes by requiring the user to be logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function



#handles user registration and stores login state in the session
@app.route("/register",methods=["GET", "POST"])
def register():
    error =None
    if request.method == "POST":
        #get username and password from form, and strip whitespace
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        #check if username is already taken
        if not username or not password:
            error = "Username and password are required."
            #make sure neither field is empty
        elif username in USERS:
            error = "Username already exists."
        else:
            #save new user to the users dictionary
            USERS[username] = password
            #log them in automatically
            session["logged_in"] = True
            session["username"] = username
            #send to homepage after registration
            return redirect(url_for("home"))
        # show the register page with any error message
    return render_template("register.html", error=error)

#handles user login and stores login state in the session
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username in USERS and USERS[username] == password:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)


#logs the user out by clearing the session
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


#this is the homepage, which will display the different questionnaires to choose from
@app.route("/")
@login_required
def home():
    return render_template("home.html", tests=TEST_URL.keys(), display_names=DISPLAY_NAMES)


#this opens the page for whichever test the user clicks on, and passes the questions, scale, and prompt to the HTML template
@app.route("/questionnaires/<test_id>")
@login_required
def test_page(test_id):

    #get the matching questionnaire file
    module = TEST_URL.get(test_id)

    #if the test name doesn't exist go back home
    if not module:
        return redirect(url_for("home"))

    #get the questions, answer scale and instructions from that file
    questions_list, scale, prompt = module.questions()

    #this sets the highest allowed answer for each test
    scale_max = {"depression": 3, "anxiety": 3, "adhd": 4, "ptsd": 4, "bipolar": 1}
    max_val = scale_max.get(test_id, 4)

    #load the check in page and send the test data into html
    return render_template(
        "check_in.html",
        questions=questions_list,
        scale=scale,
        prompt=prompt,
        test_id=test_id,
        max_val=max_val,
        display_names=DISPLAY_NAMES
    )


#this handles submitted answers
@app.route("/checkin", methods=["POST"])
def checkin():

    #this handles answers coming from the website form
    if request.form:
        #get the test name from the hidden form field
        test_id = request.form.get("test_id")

        #start each category at 0
        totals = {"stressed": 0, "happy": 0, "motivation": 0}

        #this sets the max allowed number for each test
        scale_max = {"depression": 3, "anxiety": 3, "adhd": 4, "ptsd": 4, "bipolar": 1}
        max_val = scale_max.get(test_id, 4)

        #go through every answer submitted in the form
        for key, value in request.form.items():
            #skip the hidden test_id field, only process answer fields
            if key == "test_id":
                continue

            for relevant_mood in totals.keys():
                if key.startswith(relevant_mood):
                    answer = int(value)

                    #make sure the answer is in range allowed
                    if answer < 0 or answer > max_val:
                        return render_template(
                            "check_in.html",
                            questions=TEST_URL[test_id].questions()[0],
                            scale=TEST_URL[test_id].questions()[1],
                            prompt=TEST_URL[test_id].questions()[2],
                            test_id=test_id,
                            max_val=max_val,
                            display_names=DISPLAY_NAMES,
                            error="Invalid input: values must be between 0 and {}".format(max_val)
                        )

                    #add the answer to the correct category total
                    totals[relevant_mood] += answer

        #calculate the final result from totals
        mood = calculate_mood(
            totals["stressed"],
            totals["happy"],
            totals["motivation"],
            test_id
        )

        #save web-based check-ins to the database
        username = session.get("username", "demo")
        save_checkin(
            username,
            test_id,
            totals["stressed"],
            totals["happy"],
            totals["motivation"],
            mood
        )

        #show the result page
        return render_template("results.html", mood=mood)

    #json data not form data (used by CLI client / API)
    else:
        data = request.json or {}

        mood = calculate_mood(
            data["stressed"],
            data["happy"],
            data["motivation"],
            data["test_id"]
        )

        #log JSON-based check-ins too
        username = session.get("username", "api_user")
        save_checkin(
            username,
            data["test_id"],
            data["stressed"],
            data["happy"],
            data["motivation"],
            mood
        )

        return jsonify({"mood": mood})


@app.route("/history")
@login_required
def history():
    username = session.get("username")
    records = get_checkins_by_user(username)
    return render_template(
        "history.html",
        records=records,
        username=username,
        display_names=DISPLAY_NAMES
    )


#run the flask app!
if __name__ == "__main__":
    app.run(port=5000, debug=True)
