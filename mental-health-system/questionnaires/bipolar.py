# returns the bipolar questionnaire data
def questions():
    # Based on the MDQ instrument
# instructions shown before the questions
    prompt = "Has there ever been a period of time when you were not your usual self and…"

    # list of questions
    # id = question number
    # text = the question
    # relevant_mood = category used for scoring
    info = [
        {"id": 1,
         "text": "you felt so good or so hyper that other people thought you were not your normal self or you were so hyper that you got into trouble?",
         "relevant_mood": "happy"},
        {"id": 2,
         "text": "you were so irritable that you shouted at people or started fights or arguments?",
         "relevant_mood": "happy"},
        {"id": 3,
         "text": "you felt much more self-confident than usual?",
         "relevant_mood": "happy"},
        {"id": 4,
         "text": "you got much less sleep than usual and found you didn’t really miss it?",
         "relevant_mood": "motivation"},
        {"id": 5,
         "text": "you were much more talkative or spoke faster than usual?",
         "relevant_mood": "motivation"},
        {"id": 6,
         "text": "thoughts raced through your head or you couldn’t slow your mind down?",
         "relevant_mood": "stressed"},
        {"id": 7,
         "text": "you were so easily distracted by things around you that you had trouble concentrating or staying on track?",
         "relevant_mood": "stressed"},
        {"id": 8,
         "text": "you had much more energy than usual?",
         "relevant_mood": "motivation"},
        {"id": 9,
         "text": "you were much more active or did many more things than usual?",
         "relevant_mood": "motivation"},
        {"id": 10,
         "text": "you were much more social or outgoing than usual, for example, you telephoned friends in the middle of the night?",
         "relevant_mood": "motivation"},
        {"id": 11,
         "text": "you did things that were unusual for you or that other people might have thought were excessive, foolish, or risky?",
         "relevant_mood": "motivation"},
        {"id": 12,
         "text": "spending money got you or your family in trouble?",
         "relevant_mood": "stressed"}
    ]
    # this test uses yes/no answers
    scale = "0: No, 1: Yes"

    # return all questionnaire data
    return info, scale, prompt