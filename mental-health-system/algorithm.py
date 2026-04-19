# I changed the algorithm to use the raw score for results like in the original tests,
# but also sum up the relevant mood scores so that it still makes a specific result response
# The range logic involves how many questions in general there are, how many questions related to a
# specific mood there are, and the scale number

def calculate_mood(stressed, happy, motivation, test_id):

    raw_score = stressed + happy + motivation
    feedback = [] # I wanted to allow for different responses to be said in the same result sentence if
    # two or more mood scores were equivalent or in the same range

    # To better explain the range logic, for example in the depression test there are 9 questions,
    # 3 related to each mood, and the scale is 0-3, so the max score for each mood is 9
    # I split the max mood score in all the tests into three different ranges that indicate low, moderate, and high scores
    # as I know that the same raw score can be made from different combinations of mood scores,
    # and it'd make it possible to give feedback specifically made for those variations of mood scores in their
    # respective tests and severity levels

    if test_id == "depression":
        if raw_score in range(0,5):
            if stressed in range(0,4) and happy in range(0,4) and motivation in range(0,4):
                feedback.append("to be doing okay")
            if stressed in range(4,7):
                feedback.append("a bit stressed")
            if happy in range(4,7):
                feedback.append("a bit upset about something")
            if motivation in range(4,7):
                feedback.append("like you might need some inspiration")

            if feedback:
                return "Your depression level is minimal, but you seem " + " ".join(feedback)
            else:
                return "Your depression level is minimal."

        elif raw_score in range(5,10):
            if stressed in range(4,7):
                feedback.append("kinda stressed")
            if happy in range(4,7):
                feedback.append("a bit in the blues")
            if motivation in range(4,7):
                feedback.append("to lack motivation")

            if feedback:
                return "Your depression level is mild, and you seem " + " ".join(feedback)
            else:
                return "Your depression level is mild."

        elif raw_score in range(10,15):
            if stressed in range(4,7):
                feedback.append("pretty tense")
            if happy in range(4,7):
                feedback.append("down in the dumps")
            if motivation in range(4,7):
                feedback.append("pretty low on energy")

            if feedback:
                return "Your depression level is moderate, and you seem " + " ".join(feedback)
            else:
                return "Your depression level is moderate."

        elif raw_score in range(15,20):
            if stressed in range(7,10):
                feedback.append("overwhelmed with stress")
            if happy in range(7,10):
                feedback.append("pretty gloomy")
            if motivation in range(7,10):
                feedback.append("demotivated")

            if feedback:
                return "Your depression level is moderately severe, and you seem " + " ".join(feedback)
            else:
                return "Your depression level is moderately severe."

        else:
            if stressed in range(7,10):
                feedback.append("exhausted")
            if happy in range(7,10):
                feedback.append("drained")
            if motivation in range(7,10):
                feedback.append("downhearted")

            if feedback:
                return "Your depression level is severe, and you seem " + " ".join(feedback)
            else:
                return "Your depression level is severe."

    elif test_id == "anxiety":
        if raw_score in range(0,5):
            if stressed in range(0,6) and happy == 0:
                feedback.append("to be doing okay")
            if stressed in range(6,12):
                feedback.append("a bit tense")
            if happy == 1:
                feedback.append("a little uneasy")

            if feedback:
                return "Your anxiety level is minimal, but you seem " + " ".join(feedback)
            else:
                return "Your anxiety level is minimal."

        elif raw_score in range(5,10):
            if stressed in range(6,12):
                feedback.append("sort of frantic")
            if happy == 1:
                feedback.append("kinda antsy")

            if feedback:
                return "Your anxiety level is mild, and you seem " + " ".join(feedback)
            else:
                return "Your anxiety level is mild."

        elif raw_score in range(10,15):
            if stressed in range(12,19):
                feedback.append("pretty unsettled")
            if happy in range(2,4):
                feedback.append("pent-up")

            if feedback:
                return "Your anxiety level is moderate, and you seem " + " ".join(feedback)
            else:
                return "Your anxiety level is moderate."

        else:
            if stressed in range(12,19):
                feedback.append("extremely worried")
            if happy in range(2,4):
                feedback.append("agitated")

            if feedback:
                return "Your anxiety level is severe, and you seem " + " ".join(feedback)
            else:
                return "Your anxiety level is severe."

    elif test_id == "adhd":
        if raw_score in range(0,24):
            if motivation in range(0,15) and stressed in range(0,8) and happy == 0:
                feedback.append("to be doing okay")
            if motivation in range(15,30):
                feedback.append("like you have trouble focusing")
            if stressed in range(8,16):
                feedback.append("a bit unsettled")
            if happy in range(1,3):
                feedback.append("to get carried away with things")

            if feedback:
                return "Your ADHD level is mild, but you seem " + " ".join(feedback)
            else:
                return "Your ADHD level is mild."

        elif raw_score in range(24,48):
            if motivation in range(15,30):
                feedback.append("kinda inattentive")
            if stressed in range(8,16):
                feedback.append("sort of restless")
            if happy in range(1,3):
                feedback.append("overwhelmingly enthusiastic")

            if feedback:
                return "Your ADHD level is moderate, and you seem " + " ".join(feedback)
            else:
                return "Your ADHD level is moderate."

        else:
            if motivation in range(30,45):
                feedback.append("extremely inattentive")
            if stressed in range(16,25):
                feedback.append("very restless")
            if happy in range(3,5):
                feedback.append("hyped up")

            if feedback:
                return "Your ADHD level is severe, and you seem " + " ".join(feedback)
            else:
                return "Your ADHD level is severe."

    elif test_id == "ptsd":
        if raw_score in range(0,20):
            if stressed in range(0,12) and happy in range(0,10) and motivation in range(0,6):
                feedback.append("to be doing okay")
            if stressed in range(12,24):
                feedback.append("a bit tense")
            if happy in range(10,19):
                feedback.append("like something is troubling you")
            if motivation in range(6,11):
                feedback.append("like you have moments of withdrawal")

            if feedback:
                return "Your PTSD level is minimal, but you seem " + " ".join(feedback)
            else:
                return "Your PTSD level is minimal."

        elif raw_score in range(20,40):
            if stressed in range(12,24):
                feedback.append("a bit on edge")
            if happy in range(10,19):
                feedback.append("kinda upset about something")
            if motivation in range(6,11):
                feedback.append("a bit withdrawn")

            if feedback:
                return "Your PTSD level is mild, and you seem " + " ".join(feedback)
            else:
                return "Your PTSD level is mild."

        elif raw_score in range(40,60):
            if stressed in range(24,37):
                feedback.append("tensed up")
            if happy in range(19,29):
                feedback.append("pretty distraught about something")
            if motivation in range(11,17):
                feedback.append("pretty numb")

            if feedback:
                return "Your PTSD level is moderate, and you seem " + " ".join(feedback)
            else:
                return "Your PTSD level is moderate."

        else:
            if stressed in range(24,37):
                feedback.append("very uneasy")
            if happy in range(19,29):
                feedback.append("extremely disturbed about something")
            if motivation in range(11,17):
                feedback.append("desensitized")

            if feedback:
                return "Your PTSD level is severe, and you seem " + " ".join(feedback)
            else:
                return "Your PTSD level is severe."

    elif test_id == "bipolar":
        if raw_score in range(0,4):
            if stressed == 0 and happy == 0 and motivation in range(0,2):
                feedback.append("to be doing okay")
            if stressed == 1:
                feedback.append("a bit tense")
            if happy == 1:
                feedback.append("a bit hyped up")
            if motivation in range(2,4):
                feedback.append("a little impulsive")

            if feedback:
                return "Your bipolar symptom level is mild, but you seem " + " ".join(feedback)
            else:
                return "Your bipolar symptom level is mild."

        elif raw_score in range(4,8):
            if stressed == 1:
                feedback.append("kinda overstimulated")
            if happy == 1:
                feedback.append("kinda hyperactive")
            if motivation in range(2,4):
                feedback.append("pretty spontaneous")

            if feedback:
                return "Your bipolar symptom level is moderate, and you seem " + " ".join(feedback)
            else:
                return "Your bipolar symptom level is moderate."

        else:
            if stressed in range(2,4):
                feedback.append("extremely overstimulated")
            if happy in range(2,4):
                feedback.append("pretty excitable")
            if motivation in range(4,7):
                feedback.append("pretty impetuous")

            if feedback:
                return "Your bipolar symptom level is severe, and you seem " + " ".join(feedback)
            else:
                return "Your bipolar symptom level is severe."
    else:
        return "Invalid test ID"