# returns the depression questionnaire data
def questions():
    # Based on the PHQ-9 instrument
    # instructions shown before the questions
    prompt = "Over the last 2 weeks, how often have you been bothered by any of the following problems?:"

    # list of questions
    # id = question number
    # text = the question
    # relevant_mood = category used for scoring
    info = [
        {"id": 1,
         "text": "Little interest or pleasure in doing things",
         "relevant_mood": "motivation"},
        {"id": 2,
         "text": "Feeling down, depressed, or hopeless",
         "relevant_mood": "happy"},
        {"id": 3,
         "text": "Trouble falling or staying asleep, or sleeping too much",
         "relevant_mood": "stressed"},
        {"id": 4,
         "text": "Feeling tired or having little energy",
         "relevant_mood": "motivation"},
        {"id": 5,
         "text": "Poor appetite or overeating",
         "relevant_mood": "stressed"},
        {"id": 6,
         "text": "Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
         "relevant_mood": "happy"},
        {"id": 7,
         "text": "Trouble concentrating on things, such as reading the newspaper or watching television",
         "relevant_mood": "motivation"},
        {"id": 8,
         "text": "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual",
         "relevant_mood": "stressed"},
        {"id": 9,
         "text": "Thoughts that you would be better off not existing or hurting yourself in some way",
         "relevant_mood": "happy"}
    ]
    
    # answer scale shown to the user
    scale = "0: Not At All, 1: Several Days, 2: More Than Half The Days, 3: Nearly Every Day"
   
    # return all questionnaire data
    return info, scale, prompt