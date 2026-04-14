import sys
from client import send_checkin
from questionnaires import depression, anxiety, adhd, ptsd, bipolar

# Will update this file once the algorithm and formulas are determined

def main():
    print("Hello! Welcome to the Mental Health Check-In System!")
    print("1. Depression Check-In")
    print("2. Anxiety Check-In")
    print("3. ADHD Check-In")
    print("4. PTSD Check-In")
    print("5. Bipolar Disorder Check-In")
    print("6. Exit")

    choice = input("Which check-in will you be completing?: ")

    if choice == "1":
        s, h, m = depression.questions()
        send_checkin(s, h, m, "depression")
    elif choice == "2":
        s, h, m = anxiety.questions()
        send_checkin(s, h, m, "anxiety")
    elif choice == "3":
        s, h, m = adhd.questions()
        send_checkin(s, h, m, "adhd")
    elif choice == "4":
        s, h, m = ptsd.questions()
        send_checkin(s, h, m, "ptsd")
    elif choice == "5":
        s, h, m = bipolar.questions()
        send_checkin(s, h, m, "bipolar")
    elif choice == "6":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
