import requests
from os import getenv
from time import sleep
from concurrent.futures import ThreadPoolExecutor

from workspace import SlackWorkspace
from users import Users
from post_message import post_message
from exceptions import get_users_exception, missing_token

def token(token_name="SLACK_TOKEN") -> SlackWorkspace:
    try:
        workspace = SlackWorkspace(token_name).validate_token()
    except missing_token.MissingToken as error:
        print(error)
        x = missing_token.MissingToken.add_token()
        return token(token_name=x)
    return workspace

workspace = token()
users = Users()

try:
    data = workspace.get_users().get_json()
except Exception as error:
    print(error)

if not data["ok"]:
    print(data)
    exit()

print("Found " + len(data["members"]) + "members.")

with ThreadPoolExecutor(max_workers=4) as tpe:
    tpe.map(post_message, ("test message", data, users, workspace))
