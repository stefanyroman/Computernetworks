import requests
def send_checkin(stressed, happy, motivation):

    data = {
        "stressed": stressed,
        "happy": happy,
        "motivation": motivation,
    }

    response = requests.post("http://127.0.0.1:5000/checkin", json=data)

    print("Server Response:", response.json())