import requests
def send_checkin(stressed, happy, motivation):

    data = {
        "stressed": stress,
        "happy": happy,
        "motivation": motivation,
    }

    response = request.post("http://127.0.0.1:5000/checkin", json=data)

    print("Server Response:", response.json())