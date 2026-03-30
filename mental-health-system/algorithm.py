def calculate_mood(stressed, happy, motivation):
    # (See main.py for more context on the score update)
    # Adjusted the inputs used in main.py to expand the algorithmic aspect of the project; likely needs more work done

    score = (happy + motivation) - stressed

    if score > 10:
        return "Positive"
    elif score >= 0:
        return "Neutral"
    else:
        return "Needs Help - Check in :( "