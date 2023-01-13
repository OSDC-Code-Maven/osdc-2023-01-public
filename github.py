import requests
import sys
from pprint import pprint


def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    return user_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(f"Usage {sys.argv[0]} USERNAME")
    username = sys.argv[1]
    pprint(get_user_info(username))

