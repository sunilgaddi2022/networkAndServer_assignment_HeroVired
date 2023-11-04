import requests
import time
from prettytable import PrettyTable

# Subdomains list to check the status
subdomains = [
    "chat.openai.com",
    "www.gmail.com",
    "www.herovired.com",
    "vlearnv.herovired.com",
    "subdomain1.example.com"
]

table = PrettyTable()
table.field_names = ["Subdomain", "Status"]

def status_check(subdomain):
    try:
        response = requests.get(f"https://{subdomain}", timeout=10)  # Use HTTPS and add a timeout
        if response.status_code == 200:
            return "Up"
        else:
            return "Down"
    except (requests.ConnectionError, requests.Timeout):
        return "Down"
    except Exception as e:
        return f"Error: {e}"

def store_data_in_table():
    table.clear_rows()
    for subdomain in subdomains:
        status = status_check(subdomain)
        table.add_row([subdomain, status])

def main():
    try:
        while True:
            store_data_in_table()
            print(table)
            time.sleep(60)  # Check every minute (adjust as needed)
    except KeyboardInterrupt:
        print("Status check interrupted by the user.")

if __name__ == "__main__":
    main()
