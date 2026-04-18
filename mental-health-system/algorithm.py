# The weights are meant to have each mood category add to the score
# in a way that aligns with how relevant a mood is in a test, which is why they add up to 1
# as it's meant to reflect how percentages work in dividing up sections.

weights = {
    "adhd": {"stressed": 0.25, "happy": 0.10, "motivation": 0.65},
    "anxiety": {"stressed": 0.70, "happy": 0.10, "motivation": 0.20},
    "depression": {"stressed": 0.30, "happy": 0.45, "motivation": 0.25},
    "ptsd": {"stressed": 0.60, "happy": 0.20, "motivation": 0.20},
    "bipolar": {"stressed": 0.20, "happy": 0.50, "motivation": 0.30}
}

def calculate_mood(stressed, happy, motivation, test_id):

    # To allow the test to give feedback that aligns with both the original tests and the mood categories,
    # the weights are multiplied by the user's actual responses and added together to make the score
    score = (
        weights[test_id]["stressed"] * stressed +
        weights[test_id]["happy"] * happy +
        weights[test_id]["motivation"] * motivation
    )

    # Feedback is based on results from the original tests; however, this will be updated to have better responses

    if test_id == "depression":
        if score < 5:
            return "minimal"
        elif score < 10:
            return "mild"
        elif score < 15:
            return "moderate"
        elif score < 20:
            return "moderately severe"
        else:
            return "severe"
    elif test_id == "anxiety":
        if score < 5:
            return "minimal"
        elif score < 10:
            return "mild"
        elif score < 15:
            return "moderate"
        else:
            return "severe"
    elif test_id == "adhd":
        if score < 12:
            return "mild"
        elif score < 20:
            return "moderate"
        else:
            return "severe"
    elif test_id == "ptsd":
        if score < 20:
            return "minimal"
        elif score < 40:
            return "moderate"
        else:
            return "severe"
    elif test_id == "bipolar":
        if score < 10:
            return "mild"
        elif score < 18:
            return "moderate"
        else:
            return "severe"
    else:
        return "Invalid test ID"