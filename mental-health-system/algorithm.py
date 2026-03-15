def calculate_mood(stressed, happy, motivation):
    score = (happy + motivation) - stressed

    if score > 5:
        return "Positive"
    elif score >= 0:"
        return "Neutral"
    else:
        return "Needs Help - Check in :( "
