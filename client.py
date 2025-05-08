
import requests
import time
from datetime import datetime
import pytz
import os

TIMEZONE_IST = pytz.timezone('Asia/Kolkata')
SERVER_IP = 'http://91.99.6.15:8001/status/allen'
REQUEST_TIMEOUT = 2
SLEEP_TIME = 1

def get_status():
    try:
        os.system('clear')
        
        response = requests.get(SERVER_IP, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()

        # Parse the UTC expiry timestamp
        utc_time = datetime.fromisoformat(data["expires"].replace("Z", "+00:00"))

        # Convert to IST
        ist_time = utc_time.astimezone(TIMEZONE_IST)

        print(f"Status: {data['status']}")
        print(f"🕒 Expires at (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}")

        if data['status'] != "true":
            print("Locked!")
            print('\a')
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("❌ Status not found")
            print("Locked!")
            print('\a')
        elif response.status_code == 410:
            print("⚠️ Status expired")
            print("Locked!")
            print('\a')
        else:
            print("❌ Server error:", err)
    except Exception as e:
        print("❌ Error fetching status:", e)

if __name__ == "__main__":
    while True:
        get_status()
        time.sleep(SLEEP_TIME)
