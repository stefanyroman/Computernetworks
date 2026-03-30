from client import send_checkin


def main():
    print("Hello :) This is your Mental Health Check-In!")

    # Instead of asking users to give a number on each variable, they answer common psychiatric evaluation questions
    # Based on the PHQ-9 instrument
    print("When answering the following questions, please keep in mind what each scale number means:")
    print("1: Not at all, 2: Rarely, 3: Several Days, 4: More Than Half The Days, 5: Nearly Every Day")

    q1 = int(input("On a scale of 1-5, how often do you find it hard to focus or complete tasks?: "))
    q2 = int(input("On a scale of 1-5, how often do you experience little interest or pleasure in doing things?: "))
    q3 = int(input("On a scale of 1-5, how often do you have trouble falling or staying asleep, or sleeping too much?: "))
    q4 = int(input("On a scale of 1-5, how often do you have a poor appetite or overeat?: "))
    q5 = int(input("On a scale of 1-5, how often do you feel bad about yourself or feel like a failure?: "))
    q6 = int(input("On a scale of 1-5, how often do you feel tired or have little energy?: "))
    q7 = int(input("On a scale of 1-5, how often do you become easily annoyed or irritable?: "))
    q8 = int(input("On a scale of 1-5, how often are you able to do something you enjoy?: "))
    q9 = int(input("On a scale of 1-5, how often does something make you feel satisfied, laugh, or smile?: "))

    # Questions are added to their most relevant variables to make a total used for each in algorithm.py
    stressed = (q1+q3+q4+q7)
    happy = ((6-q2)+(6-q5)+(6-q7)+q8+q9) # To keep a high total for happy as good, low amount answers are subtracted
    motivation = ((6-q2)+(6-q5)+(6-q6)) # Same as above

    send_checkin(stressed, happy, motivation)

if __name__ == "__main__":
    main()
