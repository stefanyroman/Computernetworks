from client import send_checkin


def main():
    Stressed = int(input("Stress level (1-10):"))
    Happy = int(input("Content Level (1-10)"))
    Motivation = int(input("Motivated level (1-10)"))

    send_checkin(Stressed, Happy, Motivation)
if __name__ == "__main__":
    main()
