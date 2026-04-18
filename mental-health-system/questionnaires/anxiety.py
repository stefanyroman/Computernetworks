def questions():
    # Based on the GAD-7 instrument

    prompt = "Over the last 2 weeks, how often have you been bothered by any of the following problems?:"

    info = [
        {"id": 1,
         "text": "Feeling nervous, anxious, or on edge",
         "relevant_mood": "stressed"},
        {"id": 2,
         "text": "Not being able to stop or control worrying",
         "relevant_mood": "stressed"},
        {"id": 3,
         "text": "Worrying too much about different things",
         "relevant_mood": "stressed"},
        {"id": 4,
         "text": "Trouble relaxing",
         "relevant_mood": "stressed"},
        {"id": 5,
         "text": "Being so restless that it's hard to sit still",
         "relevant_mood": "stressed"},
        {"id": 6,
         "text": "Becoming easily annoyed or irritable",
         "relevant_mood": "happy"},
        {"id": 7,
         "text": "Feeling afraid, as if something awful might happen",
         "relevant_mood": "stressed"}
    ]

    scale = "0: Not At All, 1: Several Days, 2: More Than Half The Days, 3: Nearly Every Day"

    return info, scale, prompt
