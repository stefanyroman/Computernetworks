import requests
def send_checkin(stressed, happy, motivation, test_id):

    data = {
        "test_id": test_id,
        "stressed": stressed,
        "happy": happy,
        "motivation": motivation,
    }

    try:
        response = requests.post("http://127.0.0.1:5000/checkin", json=data)

        if response.status_code == 200:
            print(response.json().get("mood"))
        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Please ensure that server.py is running.")