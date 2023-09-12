import time
import requests
from bs4 import BeautifulSoup
from plyer import notification

# URL of the webpage you want to monitor
url = "https://erdis.it/archivio-news"

# Keywords to match
keywords = ["Graduatorie", "provvisorie"]

# Function to check for keywords in the webpage
def check_for_keywords() -> bool:
    try:
        # Send a GET request to the webpage
        print("Checking for updates...")
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for the keywords in the page content
        for keyword in keywords:
            if keyword.lower() in soup.get_text().lower():
                return True
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

# Main loop to periodically check for updates
while True:
    if check_for_keywords():
        notification_title = "Graduatorie provvisorie"
        notification_message = "So uscite le graduatorie provvisorie!"
        notification.app_name = "Scholarship Notifier"
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=10
        )
        break  # Exit the loop when keywords are found

    # Wait for some time (e.g., 5 minutes) before checking again
    print("No updates found. Waiting for 30 minutes...")
    time.sleep(1800)  # 1800 seconds = 30 minutes
