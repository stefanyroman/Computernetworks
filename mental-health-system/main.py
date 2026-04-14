from client import send_checkin


def main():
    print("Hello :) This is your Mental Health Check-In!")

    # Instead of asking users to give a number on each variable, they answer common psychiatric evaluation questions
    # Based on the PHQ-9 instrument
    print("When answering the following questions, please keep in mind what each scale number means:")
    print("1: Not at all, 2: Rarely, 3: Several Days, 4: More Than Half The Days, 5: Nearly Every Day")

    while True:
        q1 = (input("On a scale of 1-5, how often do you find it hard to focus or complete tasks?: "))
        if q1 in ["1","2","3","4","5"]:
             q1= int(q1)
             break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q2 = (input("On a scale of 1-5, how often do you experience little interest or pleasure in doing things?: "))
        if q2 in ["1","2","3","4","5"]:
            q2= int(q2)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q3 = (input("On a scale of 1-5, how often do you have trouble falling or staying asleep, or sleeping too much?: "))
        if q3 in ["1","2","3","4","5"]:
            q3= int(q3)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q4 = (input("On a scale of 1-5, how often do you have a poor appetite or overeat?: "))
        if q4 in ["1","2","3","4","5"]:
            q4= int(q4)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q5 = (input("On a scale of 1-5, how often do you feel bad about yourself or feel like a failure?: "))
        if q5 in ["1","2","3","4","5"]:
            q5= int(q5)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q6 = (input("On a scale of 1-5, how often do you feel tired or have little energy?: "))
        if q6 in ["1","2","3","4","5"]:
            q6= int(q6)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q7 = (input("On a scale of 1-5, how often do you become easily annoyed or irritable?: "))
        if q7 in ["1","2","3","4","5"]:
            q7= int(q7)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q8 = (input("On a scale of 1-5, how often are you able to do something you enjoy?: "))
        if q8 in ["1","2","3","4","5"]:
            q8= int(q8)
            break
        else:
            print("!ERROR! Please choose a valid input.")
    while True:
        q9 = (input("On a scale of 1-5, how often does something make you feel satisfied, laugh, or smile?: "))
        if q9 in ["1","2","3","4","5"]:
            q9= int(q9)
            break
        else:
            print("!ERROR! Please choose a valid input.")

     # Questions are added to their most relevant variables to make a total used for each in algorithm.py
    stressed = (q1+q3+q4+q7)
    happy = ((6-q2)+(6-q5)+(6-q7)+q8+q9) # To keep a high total for happy as good, low amount answers are subtracted
    motivation = ((6-q2)+(6-q5)+(6-q6)) # Same as above

    send_checkin(stressed, happy, motivation)

if __name__ == "__main__":
    main()
