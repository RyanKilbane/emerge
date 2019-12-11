from os import getenv
import requests
from requests import Response
from exceptions import missing_token, get_users_exception
class SlackWorkspace:
    def __init__(self, token_name):
        self.token = getenv(token_name)
    
    def validate_token(self):
        if self.token == None:
            raise missing_token.MissingToken("Slack token not found in environment variables")
        elif len(self.token) == 0:
            raise missing_token.MissingToken("Slack token found, but seems to be empty")

    def get_users(self):
        workspace_users = requests.get(f"https://slack.com/api/users.list?token={self.token}")
        if workspace_users.status_code != 200:
            raise get_users_exception.GetUserException("ERROR: Cannot get list of users on workspace: " + workspace_users.text)
        return workspace_users
        
    def post_message(self):
        pass