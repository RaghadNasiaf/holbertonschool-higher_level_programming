#!/usr/bin/python3
""" Fetches data from an API """
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/1"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        print("User Name: {}".format(r.json().get("name")))
