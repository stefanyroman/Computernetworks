#allows python to send requst to server
import requests
# sends the results to the flask server
def send_checkin(stressed, happy, motivation, test_id):

    #put the data into a labled format
    data = {
        "test_id": test_id,
        "stressed": stressed,
        "happy": happy,
        "motivation": motivation,
    }

    try:
        #send the data to the server
        response = requests.post("http://127.0.0.1:5000/checkin", json=data)

        #if request works print result
        if response.status_code == 200:
            print(response.json().get("mood"))
        else:
            #if error show error code
            print(f"Error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        #this error happens when the client cannot connect to the server, likely because server.py is not running
        print("Could not connect to the server. Please ensure that server.py is running.")