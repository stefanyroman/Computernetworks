#import sys so we ccan exit program
import sys
#import function to send results to server
from client import send_checkin
#import qustionaire files
from questionnaires import depression, anxiety, adhd, ptsd, bipolar

#run1 questionnaire
def assessment(specific_checkin):
    questions, scale, prompt = specific_checkin.questions()

    print("\n" + prompt)
    print("\nWhen answering the following questions, use this scale:")
    print(scale, "\n")

    #total for each category
    stressed = 0
    happy = 0
    motivation = 0

    #go through each question and get user input
    for q in questions:
        print(f"{q['id']}: {q['text']}")
        answer = int(input("Your answer: "))

        # I realized that the moods are used for questions in conflicting ways, like how in bipolar happy is used for "you felt much more self-confident than usual"
        # but also for "you were so irritable that you shouted at people or started fights or arguments?
        # which would make it difficult to invert values here like initially planned, so I've decided that the relevant moods
        # should be considered categories in this context rather than say how happy, motivated, or stressed a user actually is

        # add to correct category
        if q["relevant_mood"] == "stressed":
            stressed += answer
        elif q["relevant_mood"] == "happy":
            happy += answer
        elif q["relevant_mood"] == "motivation":
            motivation += answer

        print()

    #sent total back
    return stressed, happy, motivation

#main menu
def main():
    print("Hello! Welcome to the Mental Health Check-In System!")
    print("1. Depression Check-In")
    print("2. Anxiety Check-In")
    print("3. ADHD Check-In")
    print("4. PTSD Check-In")
    print("5. Bipolar Disorder Check-In")
    print("6. Exit")

    #ask user which test they want
    choice = input("Which check-in will you be completing?: ")

    #run matchin questionaire 
    if choice == "1":
        s, h, m = assessment(depression)
        send_checkin(s, h, m, "depression")
    elif choice == "2":
        s, h, m = assessment(anxiety)
        send_checkin(s, h, m, "anxiety")
    elif choice == "3":
        s, h, m = assessment(adhd)
        send_checkin(s, h, m, "adhd")
    elif choice == "4":
        s, h, m = assessment(ptsd)
        send_checkin(s, h, m, "ptsd")
    elif choice == "5":
        s, h, m = assessment(bipolar)
        send_checkin(s, h, m, "bipolar")
    elif choice == "6":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main()

#start program
if __name__ == "__main__":
    main()
