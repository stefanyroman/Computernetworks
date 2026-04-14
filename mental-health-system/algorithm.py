def calculate_mood(stressed, happy, motivation, test_id):
    # Currently haven't adjusted the algorithm for the different test types,
    # Each test type could possibly have different formulas for the variables
    # because they are scaled differently and focus on different aspects of mental health

    score = (happy + motivation) - stressed

    if score > 10:
        return "Positive"
    elif score >= 0:
        return "Neutral"
    else:
        return "Needs Help - Check in :( "