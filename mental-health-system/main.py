from client import send_checkin


def main():
    print("Hello:) This is your Mental Health Check-In")

    stressed = int(input("Stress level (1-10):"))
    happy = int(input("Content Level (1-10)"))
    motivation = int(input("Motivated level (1-10)"))

    send_checkin(stressed, happy, motivation)
if __name__ == "__main__":
    main()
