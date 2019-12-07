import requests
from os import getenv
from time import sleep

from workspace import SlackWorkspace
from users import Users
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

# Is this a good idea? Should we instead build a dict keyed on email?
for member in data["members"]:
    # Filter out deleted users
    if (
        member.get("deleted", False) == False
        and member["profile"].get("email", None) != None
        and member["profile"]["email"].lower() in users
    ):
        # Rate limiting - Tier 3 (50+ per minute)
        sleep(1.2)

        print(f'{member["id"]}: {member["real_name"]}')

        rdata = {"token": workspace.token, "users": member["id"]}
        response = requests.post("https://slack.com/api/conversations.open", data=rdata)
        data = response.json()
        channel = data["channel"]["id"]

        rdata = {
            "token": workspace.token,
            "as_user": True,
            "channel": channel,
            "text": """Example message""",
        }
        response = requests.post("https://slack.com/api/chat.postMessage", data=rdata)
        status_code = response.status_code
        if status_code != 200:
            print(f"{status_code}: {response.text}")
