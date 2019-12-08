import requests
from os import getenv
from time import sleep
from concurrent.futures import ThreadPoolExecutor

from workspace import SlackWorkspace
from users import Users
from post_message import post_message
from exceptions import get_users_exception, missing_token

workspace = SlackWorkspace("SLACK_TOKEN")
users = Users()

# Lookup all members (since we can't do lookupByEmail with our legacy xoxp token)
response = requests.get(f"https://slack.com/api/users.list?token={workspace.token}")
if response.status_code != 200:
    raise get_users_exception.GetUserException("ERROR: Cannot get list of users on workspace: " + response.text)
try:
    data = response.json()
except Exception as error:
    print("ERROR: Error deserialising JSON from user.list call")
    exit(1)

if not data["ok"]:
    print(data)
    exit()

print("Found " + len(data["members"]) + "members.")
with ThreadPoolExecutor(max_workers=4) as tpe:
    tpe.map(post_message, ("test message", data, users, workspace))
    