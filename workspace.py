from os import getenv
from exceptions import missing_token
class SlackWorkspace:
    def __init__(self, token_name):
        token = self._validate_token(getenv(token_name))
    
    @staticmethod
    def _validate_token(token):
        if token == None:
            raise missing_token.MissingToken("Slack token not found in environment variables")
        elif len(token) == 0:
            raise missing_token.MissingToken("Slack token found, but seems to be empty")
