import requests
import argparse
from os import getenv
from time import sleep
from concurrent.futures import ThreadPoolExecutor

from workspace import SlackWorkspace
from users import Users, UserOperations
from post_message import post_message
from exceptions import get_users_exception, missing_token

parser = argparse.ArgumentParser(description="Emerge: A cli for spamming people on Slack")
parser.add_argument("--message", "-m", type=str, help="Message to send", required=True)
parser.add_argument("--users", "-u", type=str, help="A list of user emails", nargs="+")
parser.add_argument("--load_users", "-lu", type=str, help="Load user emails from a JSON file")
parser.add_argument("--dump_users", "-du", type=str, help="Dump user emails to a JSON file")

args = parser.parse_args()
input_users = args.users
message = args.message

if input_users is not None:
    input_users = Users(args.users)

    if args.load_users is not None:
        users = Users()
        UserOperations(args.load_users).import_users(users)
    
    if args.dump_users is not None:
        dump_path = args.dump_users
        UserOperations(dump_path).export_users(input_users)

if args.load_users is not None:
    users = Users()
    UserOperations(args.load_users).import_users(users)



def token(token_name="SLACK_TOKEN") -> SlackWorkspace:
    try:
        workspace = SlackWorkspace(token_name).validate_token()
    except missing_token.MissingToken as error:
        print(error)
        x = missing_token.MissingToken.add_token()
        return token(token_name=x)
    return workspace

workspace = token()

try:
    response = workspace.get_users().json()
except Exception as error:
    print(error)

try:
    data = workspace.validate_response(response)
except get_users_exception.GetUserException as error:
    print(error)

print("Found " + len(data["members"]) + "members.")

def post_wrapper(message, data, users, workspace):
    with ThreadPoolExecutor(max_workers=4) as tpe:
        tpe.map(post_message, (message, data, users, workspace))
