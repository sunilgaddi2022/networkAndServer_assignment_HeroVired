import requests
import time
from prettytable import PrettyTable

# Define the list of subdomains to monitor
subdomains = ["subdomain1.example.com", "subdomain2.example.com"]

# Function to check the status of a subdomain
def check_status(subdomain):
    try:
        response = requests.get(f"https://{subdomain}")
        if response.status_code == 200:
            return "Up"
        else:
            return "Down"
    except requests.exceptions.RequestException:
        return "Down"

# Function to display the status in tabular format
def display_status(subdomains_status):
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status"]
    for subdomain, status in subdomains_status.items():
        table.add_row([subdomain, status])
    print(table)

# Main loop to periodically check the status
while True:
    subdomains_status = {}
    for subdomain in subdomains:
        status = check_status(subdomain)
        subdomains_status[subdomain] = status

    display_status(subdomains_status)
    time.sleep(60)  # Wait for 60 seconds (1 minute) before checking again
