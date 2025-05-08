# client.py on Raspberry Pi
import requests
import time

SERVER_IP = 'http://91.99.6.15:8001/status/allen'
REQUEST_TIMEOUT = 2
SLEEP_TIME = 1

def get_status():
    try:
        response = requests.get(SERVER_IP, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        print(f"Server Status: {data['status']}")
    except requests.RequestException as e:
        print(f"Failed to fetch status: {e}")

if __name__ == "__main__":
    while True:
        get_status()
        time.sleep(SLEEP_TIME)  # Fetch status every 5 seconds