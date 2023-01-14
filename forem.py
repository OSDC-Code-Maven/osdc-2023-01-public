import requests
#import os
#import json

def fetch(url):
    print(url)
    if not url.startswith("https://dev.to/"):
        return

    url = url.replace("https://dev.to/", "https://dev.to/api/articles/")
    #print(url)
    # #url = 'https://dev.to/api/articles/latest?per_page=1'
    headers = {}
    headers['Accept'] = 'application/vnd.forem.api-v1+json'
    # #api_key = os.environ.get('DEV_TO_API_KEY')
    # #headers['api-key'] = api_key

    res = requests.get(url, headers = headers)
    if res.status_code != 200:
        print(f"Failed request. Status code {res.status_code}")
        print(res.text)
        return

    return res.json()


if __name__ == "__main__":
    fetch("https://dev.to/szabgab/open-source-development-courses-5d4b")
