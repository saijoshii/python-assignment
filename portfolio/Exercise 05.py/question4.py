#To run this program please install request package.
import requests
import sys

def check_website_status(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:
            print(f"The website {url} is up and running.")
        else:
            print(f"The website {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        check_website_status(sys.argv[1])
