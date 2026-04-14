def questions():
    # Based on the ASRS-v1.1 instrument

    # print("When answering the following questions, please keep in mind what each scale number means:")
    # print("0: Never, 1: Rarely, 2: Sometimes, 3: Often, 4: Very Often")
    #
    # print("Best describe how you have felt and conducted yourself over the past 6 months:")


    info = [
        {"id": 1,
         "text": "How often do you have trouble wrapping up final details of a project once the challenging parts have been done?",
         "relevant_mood": "motivation"},
        {"id": 2,
         "text": "How often do you have difficulty getting things in order when you have to do a task that requires organization?",
         "relevant_mood": "stressed"},
        {"id": 3,
         "text": "How often do you have problems remembering appointments or obligations?",
         "relevant_mood": "motivation"},
        {"id": 4,
         "text": "When you have a task that requires a lot of thought, how often do you avoid or delay getting started?",
         "relevant_mood": "motivation"},
        {"id": 5,
         "text": "How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?",
         "relevant_mood": "stressed"},
        {"id": 6,
         "text": "How often do you feel overly active and compelled to do things, like you were driven by a motor?",
         "relevant_mood": "stressed"},
        {"id": 7,
         "text": "How often do you make careless mistakes when you have to work on a boring or difficult project?",
         "relevant_mood": "motivation"},
        {"id": 8,
         "text": "How often do you have difficulty keeping your attention when you are doing boring or repetitive work?",
         "relevant_mood": "motivation"},
        {"id": 9,
         "text": "How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?",
         "relevant_mood": "motivation"},
        {"id": 10,
         "text": "How often do you misplace or have difficulty finding things at home or at work?",
         "relevant_mood": "stressed"},
        {"id": 11,
         "text": "How often are you distracted by activity or noise around you?",
         "relevant_mood": "motivation"},
        {"id": 12,
         "text": "How often do you leave your seat in meetings or other situations in which you are expected to remain seated?",
         "relevant_mood": "motivation"},
        {"id": 13,
         "text": "How often do you feel restless or fidgety?",
         "relevant_mood": "stressed"},
        {"id": 14,
         "text": "How often do you have difficulty unwinding and relaxing when you have time to yourself?",
         "relevant_mood": "stressed"},
        {"id": 15,
         "text": "How often do you find yourself talking too much when you are in social situations?",
         "relevant_mood": "happy"},
        {"id": 16,
         "text": "When you’re in a conversation, how often do you find yourself finishing the sentences of the people you are talking to, before they can finish them themselves?",
         "relevant_mood": "motivation"},
        {"id": 17,
         "text": "How often do you have difficulty waiting your turn in situations when turn taking is required?",
         "relevant_mood": "motivation"},
        {"id": 18,
         "text": "How often do you interrupt others when they are busy?",
         "relevant_mood": "motivation"}
    ]

    scale = "0: Never, 1: Rarely, 2: Sometimes, 3: Often, 4: Very Often"

    return info, scale