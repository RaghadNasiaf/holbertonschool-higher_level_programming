#!/usr/bin/python3
"""
This script fetches and prints the status code and name from a specific API.
"""
import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

print("Status Code: {}".format(response.status_code))
if response.status_code == 200:
    data = response.json()
    print("User Name: {}".format(data.get("name")))
